import random
import math
from game import Agent, Directions

class MCTSAgent(Agent):
    def __init__(self, **args):
        super().__init__(**args)
        self.simulation_depth = 5
        self.simulations_per_move = 100

    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        if not legalActions:
            return Directions.STOP

        root = MCTSNode(state, None)
        for _ in range(self.simulations_per_move):
            leaf = self.select_node(root)
            simulation_result = self.simulate(leaf.state)
            self.backpropagate(leaf, simulation_result)
        best_move = self.best_move(root)
        
        # Ensure the best move is legal; otherwise, choose a random legal action
        if best_move not in legalActions:
            best_move = random.choice(legalActions)
        
        return best_move

    def select_node(self, node):
        while not node.is_terminal_node():
            if not node.is_fully_expanded():
                return self.expand(node)
            else:
                node = node.best_child()
        return node

    def expand(self, node):
        action = node.untried_actions.pop()
        next_state = node.state.generatePacmanSuccessor(action)
        child_node = MCTSNode(next_state, node, action)
        node.children.append(child_node)
        return child_node

    def simulate(self, state):
        for _ in range(self.simulation_depth):
            if state.isWin() or state.isLose():
                break
            legalActions = state.getLegalPacmanActions()
            action = random.choice(legalActions)
            state = state.generatePacmanSuccessor(action)
        return state.getScore()

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.wins += result
            node = node.parent

    def best_move(self, root):
        best_child = max(root.children, key=lambda x: x.wins / x.visits if x.visits > 0 else -float('inf'))
        return best_child.action

class MCTSNode:
    def __init__(self, state, parent, action=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.untried_actions = state.getLegalPacmanActions()
        self.action = action

    def is_terminal_node(self):
        return self.state.isWin() or self.state.isLose()

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self):
        uct_scores = [(child.wins / child.visits) + (2 * math.log(self.visits) / child.visits) ** 0.5 for child in self.children]
        return self.children[uct_scores.index(max(uct_scores))]
