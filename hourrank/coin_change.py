# keys = [4,7]
q = int(raw_input().strip())
for a0 in xrange(q):
    n = long(raw_input().strip())
    remainder = n % 4
    lucky = False # initialised result as boolean
    if remainder ==0:
        lucky = True  # division by 4
    if remainder == 1:
        if n >= 21:  # equal is for the division by 7
            lucky = True
    if remainder == 2:
        if n >= 14:
            lucky = True
    if remainder == 3:
        if n >= 7:
            lucky = True

    if lucky: print "Yes"
    else: print "No"
