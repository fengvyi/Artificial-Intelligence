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

	int a = 0, b = 0, x = 0, y = 0;

	while (true) {
		cout << "Enter the start point - X:" << endl;
		cin >> a;
		cout << "Enter the start point - Y:" << endl;
		cin >> b;
		cout << "Enter the end point - X:" << endl;
		cin >> x;
		cout << "Enter the end point - Y:" << endl;
		cin >> y;
		bool result = DFS(a, b, x, y, maze);
		cout << "Path from (" << a << "," << b << ") to (" << x << "," << y << "): " << (result ? "YES" : "NO") << endl;
		cout << endl;
	}

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

