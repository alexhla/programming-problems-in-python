class Solution:
	def twoSum(self, values, target):
		d = {}							# declare an empty associative array
		for i,key in enumerate(values):	# iterate thru values enumerating for index
			if key in d:			# IF current value matches an existing key
				return [d[key],i]	#	 its the 2nd digit in a two sum pair
			d[target-key] = i 		# ELSE store the number that would yield the sum
		return []		# loop finished without a valid two sum pair, return nothing 

obj = Solution()
arr = [3, 2, 11, 15, 7]
num = 9
print("Target Sum: {}" .format(num))
print("From Integers: {}" .format(arr))
print("Answer: {}" .format(obj.twoSum(arr,num)))