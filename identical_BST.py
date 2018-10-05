class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSameTree(self, A, B):

		if A == None and B == None:  # if both trees are empty they are identical
			return True

		while A != None and B != None:
			print("A.val = {} --- B.val = {}" .format(A.val, B.val))
			return (A.val == B.val and  # python evaluates lazily thus when (A.val!=B.val) function immediately returns False
					self.isSameTree(A.left, B.left) and 
					self.isSameTree(A.right, B.right))

		return False


obj = Solution()

root1 = TreeNode(1) 
root1.left = TreeNode(2) 
root1.right = TreeNode(3) 
root1.left.left = TreeNode(4) 
root1.left.right = TreeNode(5) 

root2 = TreeNode(1) 
root2.left = TreeNode(22) 
root2.right = TreeNode(3) 
root2.left.left = TreeNode(4) 
root2.left.right = TreeNode(5) 

print("Answer: {}" .format(obj.isSameTree(root1, root2)))