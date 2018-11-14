class Solution:
	def bubble_sort(self, arr):
		bub_flag = 1  # bubbling will occur until finished i.e. until flag not set
		while bub_flag == 1:
			bub_flag = 0  # reset flag on each pass
			for i in range(0, len(arr)-1):  # iterate over all elements
				j = i+1
				if arr[j] < arr[i]:  # IF not in ascending order
					arr[i], arr[j] = arr[j], arr[i]  # swap pair
					bub_flag = 1  # set bubble flag
		return arr

obj = Solution()
x = [2,1,6,8,4,5,9]
print("Unsorted Array {}" .format(x))
obj.bubble_sort(x)
print("Sorted Array {}" .format(obj.bubble_sort(x)))
