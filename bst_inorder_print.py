class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def bstprint(self, A):
		
		if not A:
			return 0

		self.bstprint(A.left)
		inorderBST.append(A.val)
		self.bstprint(A.right)




obj = Solution()
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

inorderBST = []
obj.bstprint(root)
print("Inorder BST: {}" .format(inorderBST))
