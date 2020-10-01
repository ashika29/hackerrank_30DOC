# Question link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Code section:
# Hourglass sum problem
#!/bin/python3

import math
import os
import random
import re
import sys

def solve(List, n):
    mx = -1000000000
    for i in range(1,n-1):
        for j in range(1,n-1):
            sm = 0
            sm += List[i-1][j-1] + List[i-1][j] + List[i-1][j+1]
            sm += List[i][j]
            sm += List[i+1][j-1] + List[i+1][j] + List[i+1][j+1]
            #print(sm)
            mx = max(mx, sm)
    return mx

if __name__ == '__main__':
    arr = []
    n = 6

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    ans = solve(arr, n)
    print(ans)
