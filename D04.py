# Question link: https://www.hackerrank.com/challenges/30-class-vs-instance/problem
# Code section:
class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            initialAge = 0
            print("Age is not valid, setting age to 0.")
        else:
            pass
        self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1

