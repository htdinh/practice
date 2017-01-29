"""
Generate all possible moves for the queen in Chess. Input file format:

The first line contains two space-separated integers describing the respective values of n (the side length of the board) and k (the number of obstacles).
The next line contains two space-separated integers describing the respective values of rQueen and cQueen, denoting the position of the queen.
Each line i of the k subsequent lines contains two space-separated integers describing the respective values of rObstacle and cObstacle, denoting the position of obstacle .
"""
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

# vertical and horizontal boundaries
rE, cE = 0, n-cQueen  # (rQueen, n)
rW, cW = 0, 1-cQueen  # (rQueen, 1,
rN, cN = n-rQueen, 0  # (n, cQueen)
rS, cS = 1-rQueen, 0  # (1, cQueen)

# Diagonal boundaries
NE = min(cE,rN)
rNE, cNE = NE, NE

NW = min(rN, abs(cW)) # always non-negative
rNW, cNW = NW, -NW

SW = max(cW,rS)  # always non-positive value
rSW, cSW = SW, SW

SE = min(abs(rS),cE)
rSE, cSE = -SE, SE

for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    ro, co = rObstacle-rQueen, cObstacle-cQueen  # converting the obstacle into the new coordinate
    """
    Subsquently for each of the obstacle, check if the new boundaries of moves is limited by that obstacle
    """
    if ro == 0:  # for obstacles that lies in the horizontal line of moves
        if co > 0:
            if co <= cE:
                cE = co-1
        if co < 0:
            if co >= cW:
                cW = co+1
    if co == 0:  # for obstacles that lies in the vertical line of moves
        if ro > 0:
            if ro <= rN:
                rN = ro-1
        if ro < 0:
            if ro >= rS:
                rS = ro+1
    if co == ro:  # for obstacles that lies in the diagonal line Northeast-Southwest of moves
        if (co > 0) and (co <= NE):
            NE = co-1
            rNE, cNE = NE, NE
        if (co < 0) and (co >= SW):
            SW = co+1
            rSW, cSW = SW, SW

    if co == -ro: # for obstacles that lies in the other diagonal line of moves
        if (co > 0) and (co <= SE):
            SE = co-1
            rSE, cSE = -SE, SE
        if co < 0 and abs(co) <= NW:
            NW = abs(co)-1
            rNW, cNW = NW, -NW

moves = (cE-cW) + (rN-rS) + (cNE-cSW) + (cSE- cNW)  # Count the number of possible move on each dimension (already avoiding the position of the queen)
print(moves)