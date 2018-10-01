class Solution:
	def strStr(self, haystack, needle):

		if not needle:
			return 0

		for i in range(0, len(haystack) - len(needle) + 1):
			if haystack[i] == needle[0]:
				j = 1
				while j < len(needle) and haystack[i+j] == needle[j]:
					j += 1
					if j == len(needle):
						return i
		return -1

obj = Solution()
s1 = "mississippi"
s2 = "issippi"
print("Does'{}' contain '{}'?" .format(s1,s2))
print("Answer: {}" .format(obj.strStr(s1,s2)))