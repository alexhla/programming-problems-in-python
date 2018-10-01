class Solution:
	def isValid(self, s):
		if not s:
			return True

		stack = []
		for ch in s:
			if ch == '(' or ch == '[' or ch == '{':
				stack.append(ch)
			elif not stack:
				return False
			else:
				x = stack.pop()
				if ch == ')' and x != '(' or ch == ']' and x != '[' or ch == '}' and x != '{':
					return False

		return True if not stack else False

obj = Solution()
s = "([[]])()()()"
print("String of Parenthesis: {}" .format(s))
print("Answer: {}" .format(obj.isValid(s)))