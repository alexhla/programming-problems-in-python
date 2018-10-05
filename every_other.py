class Solution:
	def everyOther(self, s):
		return s[::2]

obj = Solution()
s1 = "abcdefghijklmnopqrstuvwxyz"
print("Return Every Other Char from '{}'" .format(s1))
print("Answer: {}" .format(obj.everyOther(s1)))