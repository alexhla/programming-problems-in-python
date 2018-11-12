class Solution:
	def insertion_sort(self, arr):
		for i in range(1, len(arr)):
			key = arr[i]  # key separates sorted (left side) from unsorted (right side)
			j = i-1

			while j >= 0 and key < arr[j]:  # while values to the left of the key are greater keep going
				arr[j+1] = arr[j]  # shifting elements to the right after each compare
				j -= 1

			arr[j+1] = key  # current key needs to be inserted back into the list in correct position

		return arr

obj = Solution()
x = [2,1,6,8,4,5,9]
print("Unsorted Array {}" .format(x))
obj.insertion_sort(x)
print("Sorted Array {}" .format(obj.insertion_sort(x)))
