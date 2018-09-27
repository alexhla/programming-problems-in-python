class Solution:
	def longestCommonPrefix(self, strs):
		if strs == []:
			return ""

		ans = ""
		for i, ch in enumerate(strs[0]):  # iterate over the characters of first word
			for j, s in enumerate(strs):  # iterate over the list of words
				if i >= len(strs[j]) or ch != s[i]:  # IF the first word is longer
					return ans  # OR the characters do not match return answer string
			ans += ch  # ELSE add the current character to answer

		return ans  # all words are identical or longer than first

obj = Solution()
l = ["flower","flow","flight", "flipped"]
print("List of Words: {}" .format(l))
print("Answer: {}" .format(obj.longestCommonPrefix(l)))