class Solution:
	def isPowerOfTwo(self, n):
		# slower method: multiply by 2 until reaching n
		x = 1
		while x < n:
			x *= 2
		return True if x==n else False            

		# faster method: check for only 1 bit being set by right shifting through all bits
		y = 0    
		while n > 0:
			y += (n & 0x01)
			n >>= 1
		return True if y==1 else False

obj = Solution()
num = 1024
print("Is {} a power of 2?" .format(num))
print("Answer: {}" .format(obj.isPowerOfTwo(num)))