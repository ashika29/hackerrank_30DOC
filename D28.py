# Question link: https://www.hackerrank.com/challenges/30-regex-patterns/problem
# Code:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    li = list()
    for N_itr in range(N):

        firstNameEmailID = input().strip().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        x = re.search(".*@gmail\.com$",emailID)
        if x:
            li.append(firstName)
        else:
            pass
    li.sort()
    print("\n".join(map(str,li)))
