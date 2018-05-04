'''

* Initial state begins with choosing dice d1,d2,d3 with equal probability.

         Transition Probabilities:

  die(t)   die(t + 1)    P( die(t + 1) | die(t) )
    d1         d1             1/2
    d1         d2             1/4 * 1/2
    d1         d3             1/4 * 1/2
    d1         -              1/4

    d2         d2             1/2
    d2         d1             1/4 * 1/2
    d2         d3             1/4 * 1/2
    d2         -              1/4

    d3         d3             1/2
    d3         d1             1/4 * 1/2
    d3         d2             1/4 * 1/2
    d3         -              1/4


         Emission Probabilities

   die(t)   num(t)      P( num(t) | die(t) )
    d1         1              0.6
    d1         2              0.2
    d1         3              0.2

    d2         1              0.2
    d2         2              0.6
    d2         3              0.2

    d3         1              0.2
    d3         2              0.2
    d3         3              0.6

'''

# Transition Probabilities
TP = [[0.0 for x in range(4)] for y in range(4)]
# Emission Probabilities
EP = [[0.0 for x in range(4)] for y in range(4)]
# state = [1.0/3 for x in range(4)]

# Input Sequence
seq = []

# Output Result
res = []
# Most Likely Probabilities of Sequence
mostLikely = 0.0

# Initialize TP and EP arrays
def init():
    TP[1][1] = 0.5
    TP[1][2] = 0.25 * 0.5
    TP[1][3] = 0.25 * 0.5
    TP[1][0] = 0.25

    TP[2][2] = 0.5
    TP[2][1] = 0.25 * 0.5
    TP[2][3] = 0.25 * 0.5
    TP[2][0] = 0.25

    TP[3][3] = 0.5
    TP[3][1] = 0.25 * 0.5
    TP[3][2] = 0.25 * 0.5
    TP[3][0] = 0.25

    EP[1][1] = 0.6
    EP[1][2] = 0.2
    EP[1][3] = 0.2

    EP[2][1] = 0.2
    EP[2][2] = 0.6
    EP[2][3] = 0.2

    EP[3][1] = 0.2
    EP[3][2] = 0.2
    EP[3][3] = 0.6

# Read Input Sequence
def HMM(s):
    global seq
    global res
    global mostLikely
    mostLikely = 0.0
    seq = []
    res = []
    for x in s:
        seq.append(x)
        res.append(x)

'''
def probXFromPrev(x):
    p1 = state[1] * TP[1][x]
    p2 = state[2] * TP[2][x]
    p3 = state[3] * TP[3][x]
    return (p1 + p2 + p3) / 0.75

def probEFromCur(e):
    p1 = state[1] * EP[1][e]
    p2 = state[2] * EP[2][e]
    p3 = state[3] * EP[3][e]
    return p1 + p2 + p3

def updateState():
    temp = [1.0 for x in range(4)]
    for i in range(3):
        temp[i + 1] = probXFromPrev(i + 1)

    for i in range(3):
        state[i + 1] = temp[i + 1]
'''

def dfs(dieUsed, p, die, pos):
    dieUsed.append(die)
    p *= EP[die][seq[pos]]
    pos += 1
    if pos == len(seq):
        # p *= 0.25
        global mostLikely
        if p > mostLikely:
            mostLikely = p
            for i in range(len(dieUsed)):
                res[i] = dieUsed[i]
        dieUsed.pop()
        return

    dfs(dieUsed, (p * TP[die][1])/0.75, 1, pos)
    dfs(dieUsed, (p * TP[die][2])/0.75, 2, pos)
    dfs(dieUsed, (p * TP[die][3])/0.75, 3, pos)
    dieUsed.pop()

def solve():
    p = 1.0/3
    dfs([], p, 1, 0)
    dfs([], p, 2, 0)
    dfs([], p, 3, 0)

lst = [
# Sequence 1
[1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 3],
# Sequence 2
[1, 2, 1, 1, 1, 2, 3, 3, 1, 2, 3, 3, 1, 3, 3],
# Sequence 3
[3, 2, 3, 1, 1, 3],
# Sequence 4
[3, 2, 3, 1, 1, 2, 3],
# Sequence 5
[1, 2, 1, 1, 2, 1],
# Sequence 6
[3, 3, 3, 1, 2, 3, 2, 2, 2, 2, 1]
]

init()
for i in range(len(lst)):
    print "Sequence %s = %s\r" %(i + 1, lst[i])
    HMM(lst[i])
    solve()
    print "Result = %s\rProbability = %s" %(res, mostLikely)
