class Solution:
	def squaresort(self, x):
		
		i = 0
		j = len(x)-1
		ans = []

		while i <= j:

			if abs(x[i]) > abs(x[j]):
				ans.append(x[i]**2)
				i += 1
			else:
				ans.append(x[j]**2)				
				j -= 1

		ans.reverse()
		return ans


obj = Solution()
a = [-10,-3,-1,0,1,3,5,6,9]
print("Starting Array {}" .format(a))
print("Answer {}" .format(obj.squaresort(a)))
