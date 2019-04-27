def fibonacci(N):

	"""
	Generates Fibonacci numbers less than N
	
	"""
	
	a = [0,1]
	
	for i in range(2, N):
		tmp = a[i-1]+a[i-2]
		if tmp < N:
			a.append(tmp)
		else:
			break
		
	return a
	
def sum_even(list):
	
	"""
	Calculates the sum of even numbers in the list
	"""
	
	sum = 0
	
	for number in list:
		
		if number % 2 == 0:
			
			sum += number
	
	return sum
	

print(sum_even(fibonacci(400000000)))
		
	
	