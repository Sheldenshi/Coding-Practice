#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for idx in range(len(s) - 1):
        if s[idx] == s[idx + 1]:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open('out', 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()