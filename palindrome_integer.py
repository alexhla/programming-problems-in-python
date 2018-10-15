class Solution:
	def isPalindrome(self, x):
		if x < 0:
			return False

		rnum = 0;
		temp = x;
		while temp != 0:
			rnum *= 10
			rnum += temp%10;
			temp //= 10;

		return True if x == rnum else False

	def isPalindrome2(self, x):
		s = str(x)
		rs = s[::-1]
		return True if s == rs else False


obj = Solution()
num = 12344321
print("Is {} A Palindrome" .format(num))
print("Answer-1: {}" .format(obj.isPalindrome(num)))
print("Answer-2: {}" .format(obj.isPalindrome2(num)))