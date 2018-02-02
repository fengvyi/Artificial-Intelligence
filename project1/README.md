## Tic-tac-toe
(also known as noughts and crosses or Xs and Os) is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

Players soon discover that best play from both parties leads to a draw, therefore, my algorithm makes sure the game always leads to a draw no matter which position to start with.

The steps of the algorithm go as follows:
1. Player 1 makes a move and check for wins.
2. If wins, return the result, if not, recursively call as the opponent.
3. If there is no empty slot left to make a move, it's a draw.

Run the script on Python 2.7
***

### Result
![Tic-tac-toe-result](https://github.com/fengvyi/Artificial-Intelligence/blob/master/project1/Tic-tac-toe-result.PNG)

***

## Maze
I use DFS for traversing.

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.

The steps of the algorithm go as follows:
1. Go 4 directions(up, down, left, right) from the start point.
2. Mark visited point. 
2. If hit a wall(e.g. value 1 in the maze.txt) or re-visit a point, stop searching.
3. If reached the target point, return true, else, call recursively.

Run the script on Python 2.7
***

### Result
![Maze-result](https://github.com/fengvyi/Artificial-Intelligence/blob/master/project1/Maze-result.PNG)

