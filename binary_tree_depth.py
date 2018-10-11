class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def maxdepth(self, A):
		
		if not A:
			return 0

		ldepth = self.maxdepth(A.left)
		rdepth = self.maxdepth(A.right) 

		# if (ldepth > rdepth): 
		# 	return ldepth+1
		# else: 
		# 	return rdepth+1

		return ldepth+1 if ldepth>rdepth else rdepth+1
	



obj = Solution()

root = Node(4)
# root.left = Node(2)
root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right.left = Node(1)
root.right.right = Node(3)
root.right.right.right = Node(6)



print("depth is {}" .format(obj.maxdepth(root)))