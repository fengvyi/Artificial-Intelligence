# Artificial-Intelligence ![build](https://img.shields.io/wercker/ci/wercker/docs.svg)

## Table of Contents

- [Project1 - Tic-Tac-Toe and Maze (DFS)](#project1-tic-tac-toe-and-maze)
- [Project2 - Generalized Tic-Tac-Toe (Minimax & Alpha-Beta Pruning)](#generalized-tic-tac-toe)
- [Project3 - N-Queens (Iterative Search	Algorithm)](#n-queens)
- [Project4 - MDP / HMM](#mdp-hmm)

<a name="project1-tic-tac-toe-and-maze"/>

## Project1 - Tic-Tac-Toe and Maze (DFS)
1. Implement	a	simple Tic Tac Toe game with a 3\*3 grid. Indicate if the	game is a lose, win, or draw.

2. Given a separate maze file in text format. In this maze, you can go up, down, left, or right. The maze is 81\*81 binary matrix where each line in the file represents a row and its values are separated with a space. 1 indicates a block that you cannot pass. 0 indicates a clear space that you can pass from.	  	  
Implement a	program that reads this maze and takes any two points (start and end indices)	as inputs	and	tells	whether	there	is a path	in this	maze between such points.	
  
***

<a name="generalized-tic-tac-toe"/>

## Project2 - [Generalized Tic-Tac-Toe](https://github.com/fengvyi/Generalized-Tic-Tac-Toe) (Minimax & Alpha-Beta Pruning)
A generalized Tic Tac Toe is an n\*n board game where each player chooses one of the parts X or O, and then plays in an alternate order to place his choice on the board. A player wins when he places m parts of	his	choice in	a	consecutive	order. The game may end in a draw when no one wins.	
Given m and n, the agent can play against another agent in an n\*n board and tries to place m parts in a row to win.	  

### Algorithm
Minimax with Alpha-Beta Pruning

### Evaluation function
We define an evaluation function based on the idea of counting winning
windows, which definition can be found in [this article](https://web.stanford.edu/class/cs221/2017/restricted/p-final/xiaotihu/final.pdf). I made further improvements that only update the winning windows and board scores containing the current move.

***

<a name="n-queens"/>

## Project3 - N-Queens (Iterative Search	Algorithm)
Solves N-Queen in n*n grid. Start with a random board, with one queen in each column.

### Heuristic function
min-conflicts heuristic

### Algorithm 
Iterative Search	Algorithm

### Pseudo-code
while not solved,
   * Variable selection: randomly select any conflicted queen variable
   * Operators: move queen in column
   * Value selection: min-conflicts heuristic
   * Choose a row value that conflicts the fewest queens
   * Goal test: no attacks 
   * Evaluation: c(n) = number of attacks

***

<a name="mdp-hmm"/>

## Project4 - MDP / HMM
### Project4(a): Grid World - Markov Decision Processes(MDP)
#### Grid World:
**A maze-like problem**
* The agent lives in a grid
* Walls block the agent’s path

**Noisy movement: actions do not always go as planned**
* 80% of the time, the action North takes the agent North 
  (if there is no wall there)
* 10% of the time, North takes the agent West; 10% East
* If there is a wall in the direction the agent would have been taken, the agent stays put

**The agent receives rewards each time step**
* Small “living” reward each step (can be negative)
* Big rewards come at the end (good or bad)

**Goal: maximize sum of rewards**

Implement a stochastic grid world problem given in gridA.1.csv or gridA.2.csv using MDP with the below information. Indicate v* for all cells in the grid.<br>

Discount factor = 0.9  and  Living reward = -0.01.<br>

In the given file: final states -> 1000 or -800 ; “0” -> empty cells ; “-“ -> walls<br>

| Noise | Direction |
| --- | -- |
| 60% | N |
| 15% | E |
| 10% | W |
| 15% | S |

#### Result after 100 iterations:
![](https://github.com/fengvyi/Artificial-Intelligence/blob/master/project4/project4a/Screen%20Shot%202018-04-30%20at%208.55.48%20PM.png)

### Project4(b) - Hidden Markov Models(HMM)
