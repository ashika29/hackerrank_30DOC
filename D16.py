# Question link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/
# Code:
#!/bin/python3
class solution():
    def __init__(self, string):
        self.s = string
    def solve(self):
        try:
            print(int(self.s))
        except ValueError:
            print("Bad String")
        finally:
            return 0



import sys
S = input().strip()
Answer = solution(S)
Answer.solve()
