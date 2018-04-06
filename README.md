# Artificial-Intelligence

## Project1 - Tic-Tac-Toe and Maze (DFS)
## Project2 - Generalized Tic-Tac-Toe (Minimax & Alpha-Beta Pruning)
## Project3 - N-Queens (Iterative Search	Algorithm)
Solves N-Queen in n*n grid. Start with a random board, with one queen in each column.

**Heuristic function:** min-conflicts heuristic

**Algorithm:** Iterative Search	Algorithm<br>

while not solved,
   * Variable selection: randomly select any conflicted queen variable
   * Operators: move queen in column
   * Value selection: min-conflicts heuristic
   * Choose a row value that conflicts the fewest queens
   * Goal test: no attacks 
   * Evaluation: c(n) = number of attacks

**Pseudo-code**:
```
while not solved:
        # Candidate set of queens with conflicts
        # Randomly select a conflicted queen variable
        # Set queen's current position to empty
        # Mark queen's original position - originPos
        # Try to find a min-conflict position to put the queen
        # New position - position
        # Min Conlicts - minConflicts
        # for each row - r:
            # Compute Conflicts c if put queen at r
            # If c < minConflicts:
            #   position = r
            #   minConflicts = c
            # else if c == minConflicts:
            # Escape local maxima by allowing moves with equal conflicts
            #   flip = random.randint(0, 1)
            #   if flip or position == originPos:
            #       position = r
            #       minConflicts = c
            
        # Update queen's new position
        # Update total conflicts
```
