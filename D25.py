# Question link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
# Code:
import math
def isPrime(n):
    if n <= 1:
        return False
    if n in (2,3):
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
# Enter your code here. Read input from STDIN. Print output to STDOUT
testcases = int(input())
while testcases > 0:
    if isPrime(int(input().strip())):
        print("Prime")
    else:
        print("Not prime")
    testcases -= 1
