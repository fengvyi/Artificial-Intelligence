#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
using namespace std;

// Find a path from (a, b) to (x, y) using Depth-first search
bool DFS(int a, int b, int x, int y, vector<vector<int>>& maze) {
	// Target found, return
	if (a == x && b == y) return true;
	// Hit a wall or re-visited previous cell, return
	if (maze[a][b] || a < 0 || a > 80 || b < 0 || b > 80) return false;
	// Set visited cell to 2
	maze[a][b] = 2;
	// Call recursively
	return DFS(a + 1, b, x, y, maze) || DFS(a, b + 1, x, y, maze) || DFS(a - 1, b, x, y, maze) || DFS(a, b - 1, x, y, maze);
}

int main() {
	int row = 0;
	int col = 0;
	int i;
	ifstream inFile;

	vector<vector<int>>maze(81, vector<int>(81));

	inFile.open("maze.txt");
	if (!inFile) {
		cout << "Unable to open file";
		exit(1); // terminate with error
	}

	// Initialize the matrix
	while (inFile >> i) {
		maze[row][col] = i;
		col++;
		if (col == 81) {
			row++;
			col = 0;
		}
	}

	int a = 4, b = 20, x = 79, y = 66;

	bool result = DFS(a, b, x, y, maze);
	
	cout << "Path from ("<<a<<","<<b<<") to ("<<x<<","<<y<<"): " << (result ? "True" : "False") << endl;

	// for (auto i : maze) {
	//	 for (auto j : i) {
	//	 	 cout << j << " ";
	//	 }
	//	 cout << endl;
	// }

	inFile.close();

	system("pause");

	return 0;
}

