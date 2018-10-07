class Solution:
	def intersect(self, x, y):

		return list(set(x).intersection(set(y)))

		# s1 = set(nums1)
		# s2 = set(nums2)
		# return list(s1.intersection(s2))

obj = Solution()
a1 = [1,2,2,3,4,5,16]
a2 = [2,3,5,8,9,10,1]
print("Answer: {}" .format(obj.intersect(a1,a2)))