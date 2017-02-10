#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here
min_diff = sys.maxint
a = sorted(a)
for i in xrange(1,len(a)):
    diff = a[i]-a[i-1]
    if diff<min_diff:
        min_diff=diff
print min_diff