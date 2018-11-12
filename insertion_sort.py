class Solution:
	def insertion_sort(self, arr):
		for i in range(1, len(arr)):
			key = arr[i]
			j = i-1

			while j >= 0 and key < arr[j]:
				arr[j+1] = arr[j]
				j -= 1

			arr[j+1] = key

		return arr

obj = Solution()
x = [2,1,6,8,4,5,9]
print("Unsorted Array {}" .format(x))
obj.insertion_sort(x)
print("Sorted Array {}" .format(obj.insertion_sort(x)))