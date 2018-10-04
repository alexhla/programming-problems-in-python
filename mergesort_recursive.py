def mergesort(a):
	if len(a) > 1:  # divide before conquering
		m = len(a)//2  # floor division to avoid floats
		l = a[:m]
		r = a[m:]

		mergesort(l)
		mergesort(r)

		i=0
		j=0
		k=0

		while i < len(l) and j < len(r):  # compares occur nlog(n) times
			if l[i] < r[j]:               # each time you divide 
				a[k]=l[i]
				i += 1
			else:
				a[k]=r[j]
				j += 1
			k += 1

		while i < len(l):
			a[k]=l[i]
			i += 1
			k += 1

		while j < len(r):
			a[k]=r[j]
			j += 1
			k += 1

x = [68,99,49,54,26,93,17,1,0,33,77]
print("Sorting {}" .format(x))
mergesort(x)
print("Result is {}" .format(x))


