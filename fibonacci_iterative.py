class Solution:
	def fib(self, index):	# 0 1 1 2 3 5 8 13 21 34 55...

		if index < 2:
			return index

		l2 = 0
		l1 = 1
		pos = 2
		
		while pos <= index:
			temp = l1
			l1 = temp+l2
			l2 = temp
			pos += 1

		return l1

obj = Solution()
num = 10
print("Fibonacci Number at Index: {}" .format(num))
print("Answer: {}" .format(obj.fib(num)))