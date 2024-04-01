# cse-571-game-mcts

**CSE 571 Spring 2024 Team Project: Games**
Justin Ngov, Arya Chethikattil, Logan Schipansky, Rohit Somasundaram

Our MCTS agent was created to play pacman.

In our improved MCTS we add heuristic evaluation to our simulation state in order to better choose actions which leads to a better performance.

**Sample commands on how to run the pacman game individually against the MCTS agents**
Run base MCTSAgent: python pacman.py -p MCTSAgent -l smallClassic

Run improved MCTSAgent: python pacman.py -p ImprovedMCTSAgent -l smallClassic

**Command to run the test script used to generate results**
python runTests.py
