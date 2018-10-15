class Solution:
	def isPalindrome(self, x):
		if x < 0:			# negative integers
			return False	# are not palindromes

		rnum = 0;
		temp = x;
		while temp != 0:
			rnum *= 10		  # left shift digits one place 
			rnum += temp%10;  # push least significant digit
			temp //= 10;	  # pop processed digit

		return True if x == rnum else False  # compare integers and return

	def isPalindrome2(self, x):
		s = str(x)		# convert integer to string
		rs = s[::-1]	# reverse string
		return True if s == rs else False  # compare strings and return


obj = Solution()
num = 12344321
print("Is {} A Palindrome" .format(num))
print("Answer-1: {}" .format(obj.isPalindrome(num)))
print("Answer-2: {}" .format(obj.isPalindrome2(num)))