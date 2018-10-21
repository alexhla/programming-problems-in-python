class Solution:
	def threeSum(self, arr):

		if len(arr) == 3:
			return [arr] if sum(arr)==0 else []   

		arr.sort()
		answer = []

		for i in range(0, len(arr)-3):
			if i != 0 and arr[i-1] == arr[i]:
				continue

			start = i+1
			end = len(arr)-1

			while start < end:
				temp = arr[i] + arr[start] + arr[end]
				if temp == 0:
					answer.append([arr[i], arr[start], arr[end]])
					duplicate_check = arr[start]
					while arr[start] == duplicate_check and start < end:
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