# Question link: https://www.hackerrank.com/challenges/30-sorting/problem
# Code:
#!/bin/python3
import sys

class BubbleSort():
    def __init__(self, arr, n):
        self.size  = n
        self.array = arr

    def swap(self, loc1, loc2):
        self.array[loc1], self.array[loc2] = self.array[loc2], self.array[loc1]
        self.numberOfSwaps += 1

    def sort(self):
        self.numberOfSwaps = 0
        for i in range(self.size):
            numberOfSwaps = 0
            for j in range(self.size-1):
                if (self.array[j] > self.array[j + 1]):
                    BubbleSort.swap(self,j,j+1)
                    numberOfSwaps += 1
            if (numberOfSwaps == 0):
                break
    def display(self):
        print("Array is sorted in %d swaps."%(self.numberOfSwaps))
        print("First Element: %d"%(self.array[0]))
        print("Last Element: %d"%(self.array[self.size-1]))

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
obj = BubbleSort(a,n)
obj.sort()
obj.display()
