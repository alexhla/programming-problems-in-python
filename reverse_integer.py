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
			return sign * n # recombine with sign and return

	def reverse2(self, x):
		sign = -1 if x<0 else 1
		s = str(abs(x))		# convert absolute value of int to string to avoid dash
		n = sign*int(s[::-1])	# reverse string and convert back to int adding sign last
		if (n > (2**31)-1) or (n < -2**31):  # check for overflow
			return 0
		else:
			return n

obj = Solution()
num = 123456789
print("Reversing {}" .format(num))
print("Answer-1: {}" .format(obj.reverse(num)))
print("Answer-2: {}" .format(obj.reverse2(num)))