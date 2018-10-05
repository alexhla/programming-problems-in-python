class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def preorder(self, A):
		if A == None:
			return
		print("{} " .format(A.val), end="")
		self.preorder(A.left)
		self.preorder(A.right)

	def inorder(self, A):
		if A == None:
			return
		self.inorder(A.left)
		print("{} " .format(A.val), end="")
		self.inorder(A.right)

	def postorder(self, A):
		if A == None:
			return
		self.postorder(A.left)
		self.postorder(A.right)
		print("{} " .format(A.val), end="")

obj = Solution()

root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 


print("Preorder" .format(obj.preorder(root)))
print("Inorder" .format(obj.inorder(root)))
print("Postorder" .format(obj.postorder(root)))
