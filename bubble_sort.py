class Solution:
	def bubble_sort(self, arr):
		bub_flag = 1
		while bub_flag == 1:
			bub_flag = 0
			for i in range(0, len(arr)-1):
				j = i+1
				if arr[j] < arr[i]:
					arr[i], arr[j] = arr[j], arr[i]
					bub_flag = 1
		return arr

obj = Solution()
x = [2,1,6,8,4,5,9]
print("Unsorted Array {}" .format(x))
obj.bubble_sort(x)
print("Sorted Array {}" .format(obj.bubble_sort(x)))
