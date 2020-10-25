#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    """
    *** Brute force ***
    arr = [0] * n
    for a, b, k in queries:
        for i in (a-1, b):
            arr[i] += k
        print(arr)
    return max(arr)
    """

    """
    Using Prefix Sum Algorithm
    """
    arr = [0] * (n + 2)
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    max_ele = - 10**20
    total = 0
    for x in range(1, n + 1):
        total += arr[x]
        max_ele = max(max_ele, total)

    return max_ele
    
if __name__ == '__main__':
    fptr = open(os.environ['out.txt'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
