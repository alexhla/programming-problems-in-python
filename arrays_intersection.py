class Solution:
	def intersect(self, x, y):

		# Method 1
		return list(set(x).intersection(set(y)))

		# Method 2
		s1 = set(x)
		s2 = set(y)
		return list(s1.intersection(s2))

		# Method 3
		xset = set(x)
		answer = set()
		for num in y:
			if num in xset:
				answer.add(num)
		
		return list(answer)

obj = Solution()
a1 = [1,2,2,3,4,5,16]
a2 = [2,3,5,8,9,10,1]
print("Answer: {}" .format(obj.intersect(a1,a2)))