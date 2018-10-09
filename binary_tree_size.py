class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def countnodes(self, A):
		
		if A == None:
			return 0

		# count = 1
		# count += self.countnodes(A.left)
		# count += self.countnodes(A.right)
		# return count

		# A More Compact Implementation

		return 1 + self.countnodes(A.left) + self.countnodes(A.right)


obj = Solution()
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(1)
root.right.right = Node(3)
print("Number of Tree Nodes is {}" .format(obj.countnodes(root)))