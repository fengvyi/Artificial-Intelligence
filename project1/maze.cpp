#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
using namespace std;

// Find a path from (a, b) to (x, y) using Depth-first search
bool DFS(int a, int b, int x, int y, vector<vector<int>>& maze) {
	//cout << a << "," << b << endl;
	if (a == x && b == y) return true;

	if (maze[a][b] || a < 0 || a > 80 || b < 0 || b > 80) return false;
	
	maze[a][b] = 2;

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

	while (inFile >> i) {
		maze[row][col] = i;
		col++;
		if (col == 81) {
			row++;
			col = 0;
		}
	}

	int a = 1, b = 75, x = 37, y = 77;

	bool result = DFS(a, b, x, y, maze);
	
	cout << "Result of finding path from ("<<a<<","<<b<<") to ("<<x<<","<<y<<") is:" << endl;
	cout << (result ? "True" : "False") << endl;

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

