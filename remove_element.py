class Solution:
	def removeElement(self, nums, val):
		i = 0			# 1st index 
		j = len(nums)-1 # 2nd index

		while i <= j:	# loop until pointers cross eachother
			if nums[i] == val:		# if value at 1st index is a match
				nums[i] = nums[j]	# replace with value at 2nd index
				j -= 1				# and then decrement the 2nd index
			else:
				i +=1	# only increment 1st index when it is NOT a match
						# as a 2nd index replacement may also be a match
		return i

obj = Solution()
arr = [7, 8, 1, 15, 7, 3, 3, 9, 7, 7, 7]
num = 7
print("Remove Element: {}" .format(num))
print("From Integers: {}\n" .format(arr))
print("Answer: {}" .format(obj.removeElement(arr,num)))
print("Resulting Integers: {}" .format(arr))