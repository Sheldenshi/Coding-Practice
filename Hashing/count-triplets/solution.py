#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    after = {}
    before = {}
    for ele in arr:
        after[ele] = after.get(ele, 0) + 1
    count = 0
    for ele in arr:
        after[ele] -= 1
        if ele % r == 0 and (ele // r) in before and (ele * r) in after:
            count += before[ele//r] * after[ele*r]
        before[ele] = before.get(ele, 0) + 1    
    return count
if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
