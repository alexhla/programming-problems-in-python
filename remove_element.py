class Solution:
	def removeElement(self, nums, val):
		i = 0
		j = len(nums)-1

		while i <= j:
			if nums[i] == val:
				nums[i] = nums[j]
				j -= 1
			else:
				i +=1

		return i

obj = Solution()
arr = [7, 8, 1, 15, 7, 3, 3, 9, 7, 7, 7]
num = 7
print("Remove Element: {}" .format(num))
print("From Integers: {}\n" .format(arr))
print("Answer: {}" .format(obj.removeElement(arr,num)))
print("Resulting Integers: {}" .format(arr))