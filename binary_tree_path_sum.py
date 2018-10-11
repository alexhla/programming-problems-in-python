class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

class Solution:
	def hasPathSum(self, node, s):
		
		if not node: 
			return (s == 0) 

		subSum = s - node.data  
		return self.hasPathSum(node.left, subSum) or self.hasPathSum(node.right, subSum) 	
	

obj = Solution()

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(1)
root.right.right = Node(3)
root.right.right.right = Node(6)

s = 7
print("Tree has path sum {} : {}" .format(s,obj.hasPathSum(root, s)))
