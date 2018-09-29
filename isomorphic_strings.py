class Solution:
	def isIsomorphic(self, s, t):

		if len(s) != len(t):
			return False

		d = {}
		h = {}

		for i in range(0, len(s)):

			x = s[i]
			y = t[i]

			if x not in d and y not in h:
				d[x] = [i]
				h[y] = [i]

			elif x in d and y in h:
				d[x].append(i)
				h[y].append(i)
				if d[x] != h[y]:
					return False
			else:
				return False

		return True

obj = Solution()
s1 = "paper"
s2 = "title"
print("Are '{}' and '{}' isomorphic?" .format(s1,s2))
print("Answer: {}" .format(obj.isIsomorphic(s1,s2)))