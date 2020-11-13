#!/bin/python3

import math
import os
import random
import re
import sys

def find_median(count_list, odd, median_start):
        count = 0
        for i in range(201):
            count_will_be_geq = count + count_list[i] >= median_start
            if count_will_be_geq:
                if not odd and count + count_list[i] == median_start:
                    next_val = 0
                    for j in range(i + 1, 201):
                        if count_list[j]:
                            next_val = j
                            break
                    return (i + next_val) / 2
                else:
                    return i
            count += count_list[i]
            
                
    
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count_list = [0] * 201
    for i in range(d):
        count_list[expenditure[i]] += 1
    start = 0
    end = d
        
    if d % 2 == 0:
        odd = False
        median_start = d // 2
    else:
        odd = True
        median_start = d // 2 + 1
        
    result = 0
    
    for x in expenditure[d:]:
        print("current num: {}".format(x))
        print(median_start)
        median = find_median(count_list, odd, median_start)
        print("current median: {}".format(median))
        if x >= median * 2:
            result += 1
        count_list[expenditure[start]] -= 1
        count_list[expenditure[end]] += 1
        start += 1
        end += 1
        
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
