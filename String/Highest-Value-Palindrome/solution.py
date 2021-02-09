#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    s_copy = list(s)
    l = 0
    r = len(s) - 1
    
    while l <= r:    
        if s_copy[l] != s_copy[r]:
            s_copy[l] = s_copy[r] = max(s_copy[l], s_copy[r])
            k -= 1
        l += 1
        r -= 1
    
    if k < 0:
        return '-1'
        
    l = 0
    r = len(s) - 1
    
    while l <= r:
        
        if l == r and k>0:
            s_copy[l] = '9'
        
        if s_copy[l] < '9':
            if k >= 2 and s_copy[l] == s[l] and s_copy[r] == s[r]:
                s_copy[l] = s_copy[r] = '9'
                k -= 2
            elif k>= 1 and (s_copy[l] != s[l] or s_copy[r] != s[r]):
                s_copy[l] = s_copy[r] = '9'
                k -= 1
        l += 1
        r -= 1
    return ''.join(s_copy)
