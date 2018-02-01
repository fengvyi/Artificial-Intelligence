# Tic-tac-toe
N = 3
gameBoard = [[0 for x in range(N)] for y in range(N)]
record = [[[0 for x in range(N)] for y in range(N)] for z in range(N * N + 1)]

# Check if the current player wins
def checkWin(row, col, player):
    r, c, i, j, x, y = 0, 0, 0, 0, 0, N - 1
    while r < N and gameBoard[r][col] == player:
        r += 1
    while c < N and gameBoard[row][c] == player:
        c += 1
    if row == col:
        while i < N and gameBoard[i][j] == player:
            i += 1
            j += 1
    if row == N - col - 1:
        while x < N and gameBoard[x][y] == player:
            x += 1
            y -= 1
    if r == N or c == N or i == N or x == N:
        return player
    return 0

# Make a move and check for wins
def move(row, col, player):
    gameBoard[row][col] = player
    return checkWin(row, col, player)

# Print the game board
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print '#',
            elif board[i][j] == 1:
                print 'X',
            else:
                print 'O',
        print ''

def cloneBoard(board, count):
    for i in range(len(board)):
        for j in range(len(board[i])):
            record[count][i][j] = board[i][j]

 
#  Let's play!
#  1 represents for player 1 
#  -1 represents for player 2
#  Each player makes a move and leave the next round to the opponent
# 
#  return: 0 - draw
#          1 - player 1 wins
#         -1 - player 2 wins
 
def solve(player, count):

    cloneBoard(gameBoard, count)

    if count == N * N:
        return 0
    count += 1
    
    # If win right away, then return that result!
    for i in range(N):
        for j in range(N):
            if gameBoard[i][j] == 0:
                result = move(i, j, player)
                gameBoard[i][j] = 0
                if result:
                    return player
                
    # Try to make a move
    for i in range(N):
        for j in range(N):
            if gameBoard[i][j] == 0:
                # Make a move and recursively call as the opponent, get the final result
                move(i, j, player)
                finalResult = solve(-player, count)
                # If the opponent wins, that's a 'bad' move, undo move and continue to find a better move
                if finalResult == -player:
                    gameBoard[i][j] = 0
                # If current player wins, return that result!
                elif finalResult == player:
                    gameBoard[i][j] = 0
                    return player
                # Draw
                else:
                    return 0
    # The current player has no move to make, the opponent wins
    return -player


solve(1, 0)

for i in range(N * N + 1):
    print "Round %s:" %(i)
    printBoard(record[i])

print "Draw!"
