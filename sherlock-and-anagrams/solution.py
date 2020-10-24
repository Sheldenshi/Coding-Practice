import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    substrings = {}

    # iterate over all substrings of s
    for start in range(len(s)):
        for end in range(start, len(s)):
            # initialize substring signature
            substring = [0 for _ in range(26)]
            for letter in s[start:end+1]:
                substring[ord(letter)-ord('a')] += 1
            # tuples are hashable in contrast to lists
            substring = tuple(substring)
            substrings[substring] = substrings.get(substring, 0) + 1

    result = 0
    for count in substrings.values():
        result += int(count*(count-1)/2)
    return result

if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)

        fptr.write(str(result) + '\n')

    fptr.close()