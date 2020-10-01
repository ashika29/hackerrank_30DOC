# Question link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Code section:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = bin(n).replace('0b','')
    count = 0
    maxo = 0
    for char in b:
        if char == '1':
            count += 1
        else:
            count = 0
        maxo = max(count,maxo)
    print(maxo)
