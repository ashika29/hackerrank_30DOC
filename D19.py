# Question link: https://www.hackerrank.com/challenges/30-interfaces/problem
# Code:
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        self.temp = []
    def divisorSum(self, n):
        for i in range(1,n+1):
            if n%i == 0:
                self.temp.append(i)
        return sum(self.temp)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
