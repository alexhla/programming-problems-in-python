# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

class Solution:
	def searchInsert(self, nums, target):

		for index, val in enumerate(nums):

			if target <= val:
				return index

		return len(nums)

obj = Solution()
arr = [1, 2, 3, 4, 5, 6, 8, 9]
num = 7
print("Insert Element: {}" .format(num))
print("Into Array: {}\n" .format(arr))
print("Answer: {}" .format(obj.searchInsert(arr,num)))