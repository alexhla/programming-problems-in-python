class Solution:
	def removeDuplicates(self, nums):
		if not nums:
			return 0

		i = 0
		for j in range(1, len(nums)):
			if nums[i] != nums[j]:
				i += 1
				nums[i] = nums[j]

		return i+1

obj = Solution()
arr = [0, 0, 0, 1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10]
print("Remove Duplicates From Integers: {}\n" .format(arr))
print("Answer: {}" .format(obj.removeDuplicates(arr)))
print("Resulting Integers: {}" .format(arr))