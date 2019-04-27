def sum35(N):
	
	"""
	Calculates the sum of multiples of 3 and 5 less than N
	"""
	
	sum = 0 
	
	for i in range(1, N):
		if i % 3 == 0:
			sum += i
			#print(i)
		elif i % 5 == 0:
			sum += i
			#print(i)
			
	return sum
	

print(sum35(1000))

