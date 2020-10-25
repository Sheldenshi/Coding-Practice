#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    num_apperance = [0 for _ in range(26)]
    for letter in s:
        num_apperance[ord(letter) - ord('a')] += 1
    without_zero = [x for x in num_apperance if x != 0]
    if len(set(without_zero)) == 1:
        return "YES"
    elif len(set(without_zero)) > 2:
        return "NO"
    else:
        m1 = max(without_zero)
        m2 = min(without_zero)
        if without_zero.count(m2) == 1:
            return "YES"
        if without_zero.count(m1) > 1 or m1 - m2 > 1:
            return "NO"
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['out.txt'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
