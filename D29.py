# Question link: https://www.hackerrank.com/challenges/30-bitwise-and/problem
# Code:

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n , k = map(int , input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)
