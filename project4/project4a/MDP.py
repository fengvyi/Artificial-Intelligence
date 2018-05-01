# Read From File
file = open("gridA.2.csv","r")
lines = file.read().split('\n')

# The value (utility) of a state s
V = []

for x in lines:
    r = x.split(',')
    if r[-1][-1] == '\r':
        r[-1] = r[-1][:-1]
    V.append(r)

Discount = 0.9
Living_reward = -0.01
M = len(V)
N = len(V[0])

# The value (utility) of a q-state (s,a):
Q = [[0 for x in range(N)] for y in range(M)]

# States indicating whether a Cell is a Wall/Empty/Final state
States = [[0 for x in range(N)] for y in range(M)]

# Direction functions as Enum
class Direction:
    N = 0
    E = 1
    W = 2
    S = 3

# Print current states of all cells
def printBoard(board):
    for row in board:
        for i in row:
            if i == '-':
                print '%8s' %(i),
            else:
                f = float(i)
                print '%8.2f' %(f),
        print '\r'

# Transition from state s to s'
def updateBoard():
    for r in range(M):
        for c in range(N):
            if States[r][c] == 0:
                V[r][c] = Q[r][c]

# An agent positions at (r,c) goes direction upon d
def move(r, c, d):
    x, y = r, c
    if d == Direction.N:
        # Agent Go North
        x = r - 1
        if x < 0 or States[x][y] == -1:
            x = r
    elif d == Direction.E:
        # Agent Go East
        y = c + 1
        if y >= N or States[x][y] == -1:
            y= c
    elif d == Direction.W:
        # Agent Go West
        y = c - 1
        if y < 0 or States[x][y] == -1:
            y = c
    else:
        # Agent Go South
        x = r + 1
        if x >= M or States[x][y] == -1:
            x = r

    return x, y

# Expected utility starting in s and acting optimally
def lookAhead(r, c):
    q = [0] * 4
    # Agent Go North
    x, y = move(r, c, Direction.N)
    qNorth = float(V[x][y])

    # Agent Go East
    x, y = move(r, c, Direction.E)
    qEast = float(V[x][y])

    # Agent Go West
    x, y = move(r, c, Direction.W)
    qWest = float(V[x][y])

    # Agent Go South
    x, y = move(r, c, Direction.S)
    qSouth = float(V[x][y])

    # Reward Function takes Noisy movement(actions do not always go as planned) and Discounting(prefer rewards now to rewards later) into account
    q[0] = (qNorth * 0.60 + qEast * 0.15 + qWest * 0.10 + qSouth * 0.15) * Discount
    q[1] = (qNorth * 0.10 + qEast * 0.60 + qWest * 0.15 + qSouth * 0.15) * Discount
    q[2] = (qNorth * 0.15 + qEast * 0.15 + qWest * 0.60 + qSouth * 0.10) * Discount
    q[3] = (qNorth * 0.15 + qEast * 0.10 + qWest * 0.15 + qSouth * 0.60) * Discount

    qValue = max(q)
    if qValue > 0:
        qValue += Living_reward
    return str(qValue)

# Perform one iteration
def oneSweep():
    for r in range(M):
        for c in range(N):
            if States[r][c] == 0:
                Q[r][c] = lookAhead(r, c)

    updateBoard()


def solve():
    print 'Init:\r'
    printBoard(V)
    for r in range(M):
        for c in range(N):
            if V[r][c] == '-' or V[r][c] == '-\r':
                States[r][c] = -1
            elif V[r][c] != '0' and V[r][c] != '0\r':
                States[r][c] = 1

    for i in range(100):
        oneSweep()

    print 'Values After %s iterations:\r' %(i + 1)
    printBoard(V)

solve()
