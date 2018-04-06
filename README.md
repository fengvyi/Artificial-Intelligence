# Artificial-Intelligence

## Project1 - Tic-Tac-Toe and Maze (DFS)
## Project2 - Generalized Tic-Tac-Toe (Minimax & Alpha-Beta Pruning)
## Project3 - N-Queens (Iterative Search	Algorithm)
Solves N-Queen in n*n grid. Start with a random board, with one queen in each column.

**Heuristic function:** min-conflicts heuristic

**Algorithm:** Iterative Search	Algorithm
while not solved,
   * Variable selection: randomly select any conflicted queen variable
   * Operators: move queen in column
   * Value selection: min-conflicts heuristic
   * Choose a row value that conflicts the fewest queens
   * Goal test: no attacks 
   * Evaluation: c(n) = number of attacks
