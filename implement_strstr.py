class Solution:
	def strStr(self, haystack, needle):

		if not needle:  # if needle is empty return zero
			return 0

		for i in range(0, len(haystack) - len(needle) + 1):  # iterate over the haystack until the remaining number of characters
		                                                     # left is less than the length of the needle
			if haystack[i] == needle[0]:  # if a haystack character matches the first needle character
				j = 1                     # initialize needle index to one as zero was checked above
				while j < len(needle) and haystack[i+j] == needle[j]:  # IF the needle index is less than needle length
					j += 1                                             # and its current character matches the haystack continue
					if j == len(needle):  # IF the needle index equals needle length then it is now out of bounds and the etire needle has been matched
						return i          # return the starting haystack index of the current match
		return -1  # haystack has been traversed with no match found return -1

obj = Solution()
s1 = "mississippi"
s2 = "issippi"
print("Does'{}' contain '{}'?" .format(s1,s2))
print("Answer: {}" .format(obj.strStr(s1,s2)))