# Mergesort is the best sorting algorithm for use with a linked-list

# Time  Complexity  O(nlogn)

	# Merging will require log(n) doublings from subarrays of size (1) to a single array of size length(n), 
	# where each pass will require (n) iterations to compare and sort each element

# Space Complexity  O(n)  arrays
#					O(1)  linked-list

def mergesort(a):
	if len(a) > 1:  # divide array into subarrays of length one
		m = len(a)//2  # floor division returns a truncated integer by rounding towards negative infinity
		l = a[:m]
		r = a[m:]

		mergesort(l)  # create auxillary arrays requiring O(n) memory in addition to the call stack overhead
		mergesort(r)

		i=0  # left half index
		j=0  # right half index
		k=0  # merge array index

		while i < len(l) and j < len(r):  # WHILE left and right halves both contain elements
			if l[i] < r[j]:
				a[k]=l[i]
				i += 1
			else:
				a[k]=r[j]
				j += 1
			k += 1

		while i < len(l):  # WHILE only left half contains elements
			a[k]=l[i]
			i += 1
			k += 1

		while j < len(r):  # WHILE only right half contains elements
			a[k]=r[j]
			j += 1
			k += 1

x = [68,99,49,54,26,93,17,1,0,33,77]
print("Sorting {}" .format(x))
mergesort(x)
print("Result is {}" .format(x))


