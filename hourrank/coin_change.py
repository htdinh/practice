# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
    """
    :param S: set of unit coins
    :param m: number of unit coins in the set S
    :param n: sum, total amount required to made up by unit coins
    :return: ???
    """
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]

arr = [4, 7]
m = len(arr)
q = int(raw_input().strip())
for a0 in xrange(q):
    n = long(raw_input().strip())
    if count(arr,m,n)>=1:
        print "Yes"
    else:
        print "No"
