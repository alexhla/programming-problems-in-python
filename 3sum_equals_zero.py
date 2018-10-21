class Solution:
	def threeSum(self, arr):

		if len(arr) <= 2:  # less than 3 digits, 3Sum impossible
			return []

		if len(arr) == 3:  # exactly 3 digits, loop below will not execute
			return [arr] if sum(arr)==0 else []

		arr.sort()  # sort to enable finding duplicate groups, they will always be adjacent once sorted
		answer = []

		for i in range(0, len(arr)-3):  # 1st pointer
			if i != 0 and arr[i-1] == arr[i]:  # check for overflow then duplicates
				continue

			start = i+1  # 2nd pointer
			end = len(arr)-1  # 3rd pointer

			while start < end:  # for each fixed 1st pointer iterate over 
				temp = arr[i] + arr[start] + arr[end]
				if temp == 0:
					answer.append([arr[i], arr[start], arr[end]])
					repeat_ch = arr[start]
					while arr[start] == repeat_ch and start < end: # check for duplicates then overflow
						start +=1
				elif temp < 0:
					start += 1
				elif temp > 0:
					end -= 1

		return answer

obj = Solution()
l = [-4,-1,0,1,2,3]
print("3Sums in '{}'" .format(l))
print("Answer: {}" .format(obj.threeSum(l)))