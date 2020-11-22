#!/bin/python3

import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    rank_set = sorted(list(set(ranked)), reverse=True)
    player.sort(reverse=True)
    print(player)
    j = 0
    result = []
    #rank_set = [100 50 40 20 10]
    # player = [120, 50, 25, 5]
    for x in player:
        while j < len(rank_set) and rank_set[j] > x:
            j += 1
        
        result.append(j + 1)
    
    return result[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
