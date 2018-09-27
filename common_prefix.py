class Solution:
	def longestCommonPrefix(self, strs):
		if strs == []:
			return ""

		ans = ""
		for i, ch in enumerate(strs[0]):
			for j, s in enumerate(strs):
				if i >= len(strs[j]) or ch != s[i]:
					return ans
			ans += ch

		return ans

obj = Solution()
l = ["flower","flow","flight", "flipped"]
print("List of Words: {}" .format(l))
print("Answer: {}" .format(obj.longestCommonPrefix(l)))