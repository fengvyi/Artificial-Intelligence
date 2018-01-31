#include <iostream>
#include<vector>
using namespace std;

#define N 3
vector<vector<int>>gameBoard(N, vector<int>(N, 0));
vector<vector<vector<int>>>record(10, vector<vector<int>>(N, vector<int>(N, 0)));

/* Check if the current player wins */
int checkWin(int row, int col, int player) {
	int r = 0, c = 0, i = 0, j = 0, x = 0, y = N - 1;
	while (r < N && gameBoard[r][col] == player) r++;
	while (c < N && gameBoard[row][c] == player) c++;
	if (row == col)  while (i < N && gameBoard[i][j] == player) i++, j++;
	if (row == N - col - 1) while (x < N && gameBoard[x][y] == player) x++, y--;
	return r == N || c == N || i == N || x == N ? player : 0;
}

/* Make a move and check for wins */
int move(int row, int col, int player) {
	gameBoard[row][col] = player;
	return checkWin(row, col, player);
}

/* Print the game board */
void printBoard(vector<vector<int>>& board) {
	for (auto x : board) {
		for (auto y : x) cout << (y ? y == 1 ? 'X' : 'O' : '#') << " ";
		cout << endl;
	}
}

/* 
 * Let's begin!
 *  1 represents for player 1 
 * -1 represents for player 2
 * Each player makes a move and leave the next round to the opponent
 *
 * return: 0 - draw
 *         1 - player 1 wins
 *        -1 - player 2 wins
 */
int solve(int player, int count) {
	//cout<<"Round="<<count<<" ,Player"<<(player == 1 ? 1 : 2)<<"'s Move, Game Board is"<<endl;
	//printBoard(gameBoard);
	record[count] = gameBoard;
	if (count == 9) return 0;

	count++;

	// If win right away, then return that result!
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!gameBoard[i][j]) {
				int result = move(i, j, player);
				gameBoard[i][j] = 0;
				if (result) return player;
			}
		}
	}

	// Try to make a move
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!gameBoard[i][j]) {
				// Make a move and recursively call as the opponent, get the final result
				move(i, j, player);
				int finalResult = solve(-player, count);
				// If the opponent wins, that's a 'bad' move, undo move and continue to find a better move
				if (finalResult == -player) {
					gameBoard[i][j] = 0;
				}
				// If current player wins, return that result!
				else if (finalResult == player) {
					gameBoard[i][j] = 0;
					return player;
				}
				// Draw
				else return 0;
			}
		}
	}
	// The current player has no move to make, the opponent wins
	return -player;
}


int main() {
	// cout << "Choose a start position:" << endl;
	// int pos = 0;
	// cin >> pos;
	// gameBoard[(pos - 1) / 3][(pos - 1) % 3] = 1;
	// record[1] = gameBoard;
	solve(1, 0);
	for (int i = 0; i < 10; i++) {
		cout << "Round " << i << ":" << endl;
		printBoard(record[i]);
	}
	cout << "Draw!" << endl;
	system("pause");
}
