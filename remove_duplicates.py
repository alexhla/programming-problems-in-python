class Solution:
	def removeDuplicates(self, nums): # remove duplicate numbers from a sorted list
		if not nums:  # an empty list has zero duplicates 
			return 0

		i = 0  # 1st pointer
		for j in range(1, len(nums)):  # loop with 2nd pointer to avoid index overflow
			if nums[i] != nums[j]:  # IF nums at 1st and 2nd pointers are NOT the same
				i += 1  # increment first pointer
				nums[i] = nums[j] # swap nums

		return i+1

obj = Solution()
arr = [0, 0, 0, 1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10]
print("Remove Duplicates From Integers: {}\n" .format(arr))
print("Answer: {}" .format(obj.removeDuplicates(arr)))
print("Resulting Integers: {}" .format(arr))