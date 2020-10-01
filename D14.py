# Question link: https://www.hackerrank.com/challenges/30-scope/problem
# Code section:

    def computeDifference(self):
      # Add your code here
      self.maximumDifference = -111111
      for i in range(0,len(self.__elements)-1):
          for j in range(i+1, len(self.__elements)):
              diff = abs(self.__elements[i]-self.__elements[j])
              self.maximumDifference = max(diff, self.maximumDifference)
