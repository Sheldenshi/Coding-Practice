#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr_sorted = sorted(arr)
    result = 10**20
    for idx in range(len(arr) - 1):
        if abs(arr_sorted[idx] - arr_sorted[idx+1]) < result:
            result = abs(arr_sorted[idx] - arr_sorted[idx+1])
    return result
if __name__ == '__main__':
    fptr = open(os.environ['out.txt'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
