class Solution:
	def trailingZeroes(self, n):
		# 1! = 1*1 = 1
		# 2! = 1*2 = 2
		# 3! = 1*2*3 = 6
		# 4! = 1*2*3*4 = 1*2*3*(2*2) = 24
		# 5! = 1*2*3*4*5 = 1*2*3*(2*2)*5 = 120

		# Prime Factorization
		# 5!  = 2^3 * 3^1 * 5*1
		# 10! = 2^8 * 3^4 * 5*2 * 7*1
		# 25! =
		# 125! = 

		# n! = 1*2*3*...*(n-2)*(n-1)*n

		divisor = 5
		answer = 0

		while n/divisor >= 1:
			answer += (n//divisor)
			divisor *= 5  # divisor -> 5 -> 25 -> 125 -> 625...

		return answer

obj = Solution()
x = 126
print("Trailing Zeros in '{}!'?" .format(x))
print("Answer: {}" .format(obj.trailingZeroes(x)))