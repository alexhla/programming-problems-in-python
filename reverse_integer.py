class Solution:
	def reverse(self, x):

		sign = -1 if x<0 else 1
		x = abs(x)	# floor division ALWAYS rounds down (-1//10 = -1)
		n = 0		# thus save sign and take absolute value

		while x != 0:
			n *= 10		# left shift digits one place 
			n += x%10	# push least significant digit
			x //= 10	# pop processed digit

		if n > (2**31)-1:	# check for overflow
			return 0
		else:
			return sign * n 	# recombine with sign and return

obj = Solution()
num = 123456789
print("Reversing {}" .format(num))
print("Answer-1: {}" .format(obj.reverse(num)))