# Question link: https://www.hackerrank.com/challenges/30-binary-search-trees/problem
# Code:
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def getHeight(self,root):
        lefth, righth = 0,0
        if root is None:
            return 0
        if root.left != None:
            lefth = Solution.getHeight(self,root.left)+1
        if root.right != None:
            righth = Solution.getHeight(self,root.right)+1
        return max(lefth,righth)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
