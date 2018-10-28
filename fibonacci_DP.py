class Solution:
	def fib(self, n):
		if n in memo:
			return memo[n]
		if n < 2:
			return 1
		else:
			f = self.fib(n-1) + self.fib(n-2)

		memo[n] = f
		return f

obj = Solution()
num = 10
memo = {}
print("Fibonacci Number at Index: {}" .format(num))
print("Answer: {}" .format(obj.fib(num)))