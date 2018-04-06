import random

# Read N-Queens Board From File
file = open("8-queen.txt","r")
lines = file.read().split('\n')

Board = []

for x in lines:
    r = x.split('\t')
    Board.append(r)

# Size of Board
N = len(Board)
# Total Conflicts Between Queens
totalConflicts = 0
# Position(row) of i-th Queen
qPositions = {}
# Conflicts of i-th Queen
qConflicts = {}

# Print Cureent Board
def printBoard(board):
    print 'Current Board: \n'

    print '   ',

    for i in range(N):
        if i < 10:
            print '%s  ' %(i),
        else:
            print '%s ' %(i),

    print '\n'

    for i in range(N):
        print '%s  ' %(i),
        for x in board[i]:
            c = '-'
            if x == '1':
                c = 'Q'
            print '%s  ' %(c),
        print '\n'


# Compute the Conflicts of i-th Queen
def computeConflicts(queen):
    conflict = 0

    row = qPositions[queen]
    col = queen

    # Check row
    for column in range(N):
        if column != col:
            if Board[row][column] == '1':
                conflict += 1

    # Check diagonal \
    r,c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if Board[r][c] == '1':
            conflict += 1
        r -= 1
        c -= 1

    r,c = row + 1, col + 1
    while r < N and c < N:
        if Board[r][c] == '1':
            conflict += 1
        r += 1
        c += 1

    # Check diagonal /
    r,c = row - 1, col + 1
    while r >= 0 and c < N:
        if Board[r][c] == '1':
            conflict += 1
        r -= 1
        c += 1

    r,c = row + 1, col - 1
    while r < N and c >= 0:
        if Board[r][c] == '1':
            conflict += 1
        r += 1
        c -= 1

    return conflict


# Initialize
def init():
    totalConflicts = 0
    for queen in range(N):
        print 'Queen: %s' %(queen),

        # Find the row of each queen
        for row in range(N):
            if Board[row][queen] == '1':
                qPositions[queen] = row


        # Compute the conflicts of each queen
        qConflicts[queen] = computeConflicts(queen)

        print ',Conflict: %s' %(qConflicts[queen])

        # Sum up conflicts
        totalConflicts += qConflicts[queen]


    return totalConflicts

# Update Conflicts after re-position a queen
def updateConflicts():
    totalConflicts = 0
    for queen in range(N):
        # Compute the conflicts of each queen
        qConflicts[queen] = computeConflicts(queen)
        # Sum up conflicts
        totalConflicts += qConflicts[queen]

    return totalConflicts

# Check Whether the Board is legit
def isSolved(totalConflicts):
    return totalConflicts == 0

# Main logic function
def solve():
    totalConflicts = init()
    print 'Total Conflicts = %s\n' %(totalConflicts)

    while not isSolved(totalConflicts):
        # Candidate set of queens with conflicts
        queens = []

        for i in range(N):
            if qConflicts[i] > 0:
                queens.append(i)

        # Randomly select a conflicted variable - queen
        q = random.choice(queens)
        # Set queen's current position to empty
        Board[qPositions[q]][q] = '0'
        # Mark queen's original position
        originPos = qPositions[q]
        # Try to find a min-conflict position to put the queen
        minConflicts = qConflicts[q]
        # The position we're going to put the queen
        position = qPositions[q]

        for pos in range(N):
            qPositions[q] = pos
            conflicts = computeConflicts(q)
            if conflicts < minConflicts:
                minConflicts = conflicts
                position = pos
            elif conflicts == minConflicts:
                # Escape local maxima by allowing moves with equal values
                flip = random.randint(0, 1)
                if (flip or position == originPos) and pos != originPos:
                    minConflicts = conflicts
                    position = pos

        # Update queen's new position
        qPositions[q] = position
        Board[position][q] = '1'

        # Log and update total conflicts
        print 'Move queen %s to %s' %(q, position)
        totalConflicts = updateConflicts()
        print 'Total Conflicts = %s\n' %(totalConflicts)


printBoard(Board)
solve()
printBoard(Board)
