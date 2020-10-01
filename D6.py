#Question link: https://www.hackerrank.com/challenges/30-review-loop/problem
#code section:
def solve(s):
    n = len(s)
    even, odd="",""
    for i in range(n):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    s = even+" "+odd
    return s

test = int(input())
while test > 0:
    x = str(input().strip())
    print(solve(x))
    test -= 1
