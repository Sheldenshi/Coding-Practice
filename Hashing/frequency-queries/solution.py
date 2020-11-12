#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    ele_freq = {}
    freq_count = {}
    result = []
    for i, j in queries:
        if i == 1:
            if j in ele_freq and ele_freq[j] in freq_count:
                freq_count[ele_freq[j]] -= 1
            ele_freq[j] = ele_freq.get(j, 0) + 1
            freq_count[ele_freq[j]] = freq_count.get(ele_freq[j], 0) + 1
        elif i == 2:
            if j in ele_freq and ele_freq[j] > 0:
                freq_count[ele_freq[j]] -= 1
                ele_freq[j] -= 1
                freq_count[ele_freq[j]] = freq_count.get(ele_freq[j], 0) + 1
        elif i == 3:
            if j in freq_count and freq_count[j] > 0:
                result.append(1)
            else:
                result.append(0)
    return result
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
