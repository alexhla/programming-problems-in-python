class Solution:
	def fib(self, n):

		if n < 2:
			return 1
		return self.fib(n-1) + self.fib(n-2)

obj = Solution()
num = 11
print("Fibonacci Number at Index: {}" .format(num))
print("Answer: {}" .format(obj.fib(num)))