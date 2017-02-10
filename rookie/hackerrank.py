#!/bin/python

import sys
map = {}
for idx, char in enumerate(list("hackerrank")):
    map.update({idx:char})

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here

    i = 0
    for idx, char in enumerate(list(s)):
        if char==map[i]:
            i+=1
        if i==len(map):
            break
    if i==len(map):
        print "YES"
    else:
        print "NO"
