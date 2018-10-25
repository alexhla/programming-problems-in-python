class Solution(object):
	def pascals_triangle(self, numRows):
		if numRows == 0:
			return []
		if numRows == 1:
			return [[1]]
		if numRows == 2:
			return [[1],[1,1]]

		result = [[1],[1,1]]  # start with first two rows preloaded

		for row in range(2, numRows):  # iterate over number of rows requested minus preloaded first two
			prev = row-1  # previous row is used to calculate current
			curr = [1]  # each row always starts with a 1
			for index, digit in enumerate(result[prev]):  # iterate over the last row in the triangle
				if index+1 >= len(result[prev]):  # overflow protection
					break
				curr.append(digit+result[prev][index+1]) # add together numbers from previous row

			curr.append(1)  # each row ends with a 1
			result.append(curr)  # add row t othe triangle

		return result

obj = Solution()
x = 10
print("Pascals Triangle {} Lines Deep" .format(x))
answer = obj.pascals_triangle(x)
for row in answer:
	print(row)