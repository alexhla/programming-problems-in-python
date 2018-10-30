class Solution(object):
	def containsDuplicate(self, nums):
		myset = set()

		for n in nums:
			if n in myset:
				return True
			myset.add(n)

		return False

obj = Solution()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
print("Duplicates In Integers: {}\n" .format(arr))
print("Answer: {}" .format(obj.containsDuplicate(arr)))