#include <iostream>
#include<vector>
using namespace std;

int player1 = 1;
int player2 = -1;
int N = 3;
vector<vector<int>>gameBoard(N, vector<int>(N, 0));
vector<vector<vector<int>>>record(10, vector<vector<int>>(N, vector<int>(N, 0)));


int checkWin(int row, int col, int n, int player) {
	int r = 0, c = 0, i = 0, j = 0, x = 0, y = n - 1;
	while (r < n && gameBoard[r][col] == player) r++;
	while (c < n && gameBoard[row][c] == player) c++;
	if (row == col)  while (i < n && gameBoard[i][j] == player) i++, j++;
	if (row == n - col - 1) while (x < n && gameBoard[x][y] == player) x++, y--;
	return r == n || c == n || i == n || x == n ? player : 0;
}

int move(int row, int col, int player) {
	gameBoard[row][col] = player;
	return checkWin(row, col, N, player);
}

void printBoard(vector<vector<int>>& board) {
	for (auto x : board) {
		for (auto y : x) cout << y << " ";
		cout << endl;
	}
}

int solve(int player, int count) {
	//cout<<"Round="<<count<<" ,Player"<<(player == 1 ? 1 : 2)<<"'s Move, Game Board is"<<endl;
	//printBoard(gameBoard);
	record[count] = gameBoard;
	if (count == 9) return 0;
	count++;
	bool noValidMove = true;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!gameBoard[i][j]) {
				int result = move(i, j, player);
				gameBoard[i][j] = 0;
				if (result) {
					return player;
				}

			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!gameBoard[i][j]) {
				int result = move(i, j, player);
				int finalResult = solve(-player, count);
				if (finalResult == -player) {
					gameBoard[i][j] = 0;
				}
				else if (finalResult == player) {
					gameBoard[i][j] = 0;
					return player;
				}
				else noValidMove = false;
			}
		}
	}

	if (noValidMove) return -player;
	return 0;
}


int main() {
	cout << "Choose a start position:" << endl;
	int pos = 0;
	cin >> pos;
	gameBoard[(pos - 1) / 3][(pos - 1) % 3] = 1;
	record[1] = gameBoard;
	solve(-1, 1);
	for (int i = 0; i < 10; i++) {
		cout << "Round " << i << ":" << endl;
		printBoard(record[i]);
	}
	cout << "Draw!" << endl;
	system("pause");
}