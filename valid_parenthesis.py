class Solution:
	def isValid(self, s):
		if not s:		# empty string is valid
			return True

		stack = []
		for ch in s:
			if ch == '(' or ch == '[' or ch == '{':  # push opening brackets onto stack
				stack.append(ch)
			elif not stack:  # if stack is empty then cannot pop needed closing bracket
				return False # string is invalid
			else:
				x = stack.pop()  # else pop and check if the closing bracket matches
				if ch == ')' and x != '(' or ch == ']' and x != '[' or ch == '}' and x != '{':
					return False

		return True if not stack else False # string valid only if stack is empty

obj = Solution()
s = "([[]])()()()"
print("String of Parenthesis: {}" .format(s))
print("Answer: {}" .format(obj.isValid(s)))