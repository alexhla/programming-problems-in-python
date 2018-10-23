class Solution:
	def trailingZeroes(self, n):
		# 1! = 1*1 = 1
		# 2! = 1*2 = 2
		# 3! = 1*2*3 = 6
		# 4! = 1*2*3*4 = 24
		# 5! = 1*2*3*4*5 = 120
		# n! = 1*2*3*...*(n-2)*(n-1)*n

		divisor = 5
		answer = 0

		while n/divisor >= 1:
			answer += (n//divisor)
			divisor *= 5

		return answer

obj = Solution()
x = 126
print("Trailing Zeros in '{}!'?" .format(x))
print("Answer: {}" .format(obj.trailingZeroes(x)))