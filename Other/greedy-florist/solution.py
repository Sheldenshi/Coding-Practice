#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    """
    Time Complexity:

    O(N log N)
    """
    sorted_prices = sorted(c)
    
    total = 0
    rounds = math.ceil(len(c) / k)
    left = len(c)
    for i in range(1, rounds + 1):
        if left < k:
            total += sum(sorted_prices[:left]) * i
        else:
            
            total += sum(sorted_prices[(len(c) - i * k):(len(c) - (i - 1) * k)]) * i
            left -= k
    return total

            

if __name__ == '__main__':
    fptr = open(os.environ['out.txt'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
    fptr.write(str(minimumCost) + '\n')

    fptr.close()
