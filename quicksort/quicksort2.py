#!/bin/python
def quick_sort(ar):
    if len(ar)==1:  # base case
        return ar
    pivot = ar[0]
    smaller = []
    larger = []
    combine = [pivot]
    for item in ar[1:]: # unique items
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)
    if smaller:
        smaller = quick_sort(smaller)
        combine = smaller + combine
    if larger:
        larger = quick_sort(larger)
        combine = combine + larger
    print " ".join(map(str,combine))
    return combine

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)
