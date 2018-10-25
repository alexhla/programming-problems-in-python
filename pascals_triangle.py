class Solution(object):
	def pascals_triangle(self, numRows):
		if numRows == 0:
			return []
		if numRows == 1:
			return [[1]]
		if numRows == 2:
			return [[1],[1,1]]

		result = [[1],[1,1]]

		for row in range(2, numRows):
			curr = [1]
			for index, digit in enumerate(result[row-1]):
				if index+1 >= len(result[row-1]):
					break
				curr.append(digit+result[row-1][index+1])
			curr.append(1)
			result.append(curr)

		return result

obj = Solution()
x = 7
print("Pascals Triangle {} Lines Deep" .format(x))
answer = obj.pascals_triangle(x)
for row in answer:
	print(row)