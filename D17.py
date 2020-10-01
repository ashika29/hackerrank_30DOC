# Question link: https://www.hackerrank.com/challenges/30-more-exceptions/problem
# Code:
#Write your code here
class Calculator():
    def power(self, base, exp):
        assert base > -1 and exp > -1, "n and p should be non-negative"
        return pow(base, exp)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
