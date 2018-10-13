class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def bstmin(self, A):
		
		while A.left != None:  # iterative solution will suffice
			A = A.left         # as no need to keep track of anything
		return A.val           # just traverse to left most node

obj = Solution()
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print("Number of Tree Nodes is {}" .format(obj.bstmin(root)))