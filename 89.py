def sort(values):
	for  i1 in range(len(values)):		
		for r in range(i1, len(values)):			
			if (values[i1] > values[r]):
				temp = values[i1]
				values[i1] = values[r]
				values[r] = temp
x = raw_input().rstrip()
xList = list(x)
sort(xList)
print("".join(xList))
