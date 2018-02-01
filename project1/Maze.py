# maze
file1 = open("maze.txt", "r")
read = file1.read()

# Find a path from (a, b) to (x, y) using Depth-first search
def DFS(a, b, x, y, maze):
    # Target found, return
    if a == x and b == y:
        return True
    # Hit a wall or re-visited previous cell, return
    if maze[a][b] or a < 0 or a > 80 or b < 0 or b > 80:
        return False
    # Set visited cell to 2
    maze[a][b] = 2
    # Call recursively
    return DFS(a + 1, b, x, y, maze) or DFS(a, b + 1, x, y, maze) or DFS(a - 1, b, x, y, maze) or DFS(a, b - 1, x, y, maze)


row, col = 0, 0

maze = [[0 for x in range(81)] for y in range(81)]

# Initialize the matrix
for x in read:
    if x == '1' or x == '0':
        maze[row][col] = int(x)
        col += 1
        if col == 81:
            row += 1
            col = 0

while True:
    a = input("Enter the start point - X: ")
    b = input("Enter the start point - Y: ")
    x = input("Enter the end point - X: ")
    y = input("Enter the end point - X: ")
    result = DFS(a, b, x, y, maze)
    res = "NO"
    if result:
        res = "YES"
    print "Path from (%s, %s) to (%s, %s): %s\n" %(a, b, x, y, res)
