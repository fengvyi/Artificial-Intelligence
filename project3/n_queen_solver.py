import random

file = open("8-queen.txt","r")
lines = file.read().split('\n')

Board = []

for x in lines:
    r = x.split('\t')
    Board.append(r)


N = len(Board)
totalConflicts = 0
qPositions = {}
qConflicts = {}

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
            c = '#'
            if x == '1':
                c = 'Q'
            print '%s  ' %(c),
        print '\n'


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

    
def updateConflicts():
    totalConflicts = 0
    for queen in range(N):
        #print 'Queen: %s' %(queen),
        
        # Compute the conflicts of each queen
        qConflicts[queen] = computeConflicts(queen)

        #print ',Conflict: %s' %(qConflicts[queen])

        # Sum up conflicts
        totalConflicts += qConflicts[queen]

    
    return totalConflicts  


def isSolved(totalConflicts):
    return totalConflicts == 0


def solve():

    printBoard(Board)
    totalConflicts = init()
    print 'Total Conflicts = %s\n' %(totalConflicts)
    
    while not isSolved(totalConflicts):
        
        queens = []
        
        for i in range(N):
            if qConflicts[i] > 0:
                queens.append(i)

        q = random.choice(queens)
        Board[qPositions[q]][q] = '0'
        
        originPos = qPositions[q]
        minConflicts = qConflicts[q]
        position = qPositions[q]
        
        for pos in range(N):
            qPositions[q] = pos
            conflicts = computeConflicts(q)
            if conflicts < minConflicts:
                minConflicts = conflicts
                position = pos
            elif conflicts == minConflicts:
                flip = random.randint(0, 1)
                if (flip or position == originPos) and pos != originPos:
                    minConflicts = conflicts
                    position = pos
        
        qPositions[q] = position
        
        Board[position][q] = '1'

        print 'Move queen %s to %s' %(q, position)
        
        totalConflicts = updateConflicts()
        #printBoard(Board)
        print 'Total Conflicts = %s\n' %(totalConflicts)


    
solve()
printBoard(Board)




