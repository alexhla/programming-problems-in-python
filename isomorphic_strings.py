class Solution:
	def isIsomorphic(self, s, t):

		if len(s) != len(t):  # isomorphic strings must be same length
			return False

		d = {}
		h = {}

		for i in range(0, len(s)):

			x = s[i]
			y = t[i]

			if x not in d and y not in h:  # Both chars have NOT been seen before (NOT in hash table)
				d[x] = [i]  # store index as a single element list since
				h[y] = [i]  # repeat character indices must be appended

			elif x in d and y in h:  # both chars seen before (EXIST in hash table)
				d[x].append(i)    # append new index to list
				h[y].append(i)
				if d[x] != h[y]:  # ensure chars have been seen at the same indices
					return False  # if indices do NOT match up strings are not isomorphic

			# One char has been seen before but NOT the other
			# if (x not in d and y in h) or (x in d and y not in h):
			else:  # only four possible outcomes thus else is sufficient
				return False

		return True  # strings are isomorphic return true

obj = Solution()
s1 = "paper"
s2 = "title"
print("Are '{}' and '{}' isomorphic?" .format(s1,s2))
print("Answer: {}" .format(obj.isIsomorphic(s1,s2)))