import random
import math
import util
from game import Agent, Directions

class ImprovedMCTSAgent(Agent):
    def __init__(self, **args):
        super().__init__(**args)
        self.simulation_depth = 5
        self.simulations_per_move = 50
    
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        legalActionsFiltered = []
        for action in legalActions:
            if action != Directions.STOP:
                legalActionsFiltered.append(action)
        if not legalActionsFiltered:
            return Directions.STOP

        root = ImprovedMCTSNode(state, None)
        for _ in range(self.simulations_per_move):
            leaf = self.select_node(root)
            simulation_result = self.simulate(leaf.state)
            self.backpropagate(leaf, simulation_result)
        best_move = self.best_move(root)
        
        if best_move not in legalActionsFiltered:
            best_move = random.choice(legalActionsFiltered)
        
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
        child_node = ImprovedMCTSNode(next_state, node, action)
        node.children.append(child_node)
        return child_node

    def simulate(self, state):
        SCORES=[0]
        SCORE=0
        for _ in range(self.simulation_depth):
            # SCORE=0 
            # if state.isWin() or state.isLose():
            #     break
            legalActions = state.getLegalPacmanActions()            
            for action in legalActions:
                state_2 = state.generatePacmanSuccessor(action)
                newPos = state_2.getPacmanPosition()
                newFood = state_2.getFood()
                newGhostStates = state_2.getGhostStates()
                newGhostPositions = state_2.getGhostPositions()
                newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
                newGetNumFood=state_2.getNumFood()
                SCORE=state_2.getScore()
                foods=[]
                SCORE+=newScaredTimes[0]
                # SCORE-=newGetNumFood
                # if len(newFood.asList()) < len(state.getFood().asList()):
                #     SCORE += 500
                if state_2.isWin():
                    return float('inf') 
                if newPos==state.getPacmanPosition():
                    SCORE-=1000
                if len(newFood.asList())>0:
                    if newFood.asList():
                        for x in newFood.asList():
                            foods.append(util.manhattanDistance(newPos, x))
                        SCORE += 10 / min(foods)
                if len(newFood.asList())==1:
                    for x in newFood.asList():
                            dist=(util.manhattanDistance(newPos, x))
                    SCORE-=dist*2
                if len(newGhostPositions)>0:
                    ghosts=[]
                    for x in newGhostPositions:
                        ghosts.append(util.manhattanDistance(newPos, x))
                    if min(ghosts)<2:
                        SCORE-=500
                # print(SCORE)
                SCORES.append(SCORE)
        # print(SCORE)
        return max(SCORES)
        # return state.getScore()
    
    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.wins += result
            node = node.parent

    def best_move(self, root):
        best_child = max(root.children, key=lambda x: x.wins / x.visits if x.visits > 0 else -float('inf'))
        return best_child.action

class ImprovedMCTSNode:
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