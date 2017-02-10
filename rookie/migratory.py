import sys
from collections import Counter

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
count = Counter(types)
max = 0
max_type=0
for type in range(5,0,-1):
    if count[type]>=max:
        max=count[type]
        max_type=type
print(max_type)