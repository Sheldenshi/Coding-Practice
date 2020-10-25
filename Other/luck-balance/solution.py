#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    """
    Time Complexity:

    O(N*log(N) ), O(N*K)
    """
    balance = 0
    important = []
    for idx in range(len(contests)):
        if contests[idx][1] == 0:
            balance += contests[idx][0]
        else:
            important.append(contests[idx][0])
    sorted_important = sorted(important, reverse=True)
    return sum(sorted_important[:k]) - sum(sorted_important[k:]) + balance
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
