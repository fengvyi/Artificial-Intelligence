# Artificial-Intelligence

## Project1 - Tic-Tac-Toe and Maze (DFS)
1. Implement	a	simple Tic Tac Toe game with a 3\*3 grid. Indicate if the	game is a lose, win, or draw.

2. Given a separate maze file in text format. In this maze, you can go up, down, left, or right. The maze is 81\*81 binary matrix where each line in the file represents a row and its values are separated with a space. 1 indicates a block that you cannot pass. 0 indicates a clear space that you can pass from.	  	  
Implement a	program that reads this maze and takes any two points (start and end indices)	as inputs	and	tells	whether	there	is a path	in this	maze between such points.	
  
***

## Project2 - [Generalized Tic-Tac-Toe](https://github.com/fengvyi/Generalized-Tic-Tac-Toe) (Minimax & Alpha-Beta Pruning)
A generalized Tic Tac Toe is an n\*n board game where each player chooses one of the parts X or O, and then plays in an alternate order to place his choice on the board. A player wins when he places m parts of	his	choice in	a	consecutive	order. The game may end in a draw when no one wins.	
Given m and n, the agent can play against another agent in an n\*n board and tries to place m parts in a row to win.	  

### Algorithm
Minimax with Alpha-Beta Pruning

### Evaluation function
We define an evaluation function based on the idea of counting winning
windows, which definition can be found in [this article](https://web.stanford.edu/class/cs221/2017/restricted/p-final/xiaotihu/final.pdf). I made further improvements that only update the winning windows and board scores containing the current move.

***

## Project3 - N-Queens (Iterative Search	Algorithm)
Solves N-Queen in n*n grid. Start with a random board, with one queen in each column.

### Heuristic function
min-conflicts heuristic

### Algorithm 
Iterative Search	Algorithm

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
