# Returns the number of ones in the binary representation of a (decimal) number

def count_ones(x):
	count = 0
	while x >= 1: 
		if x % 2 == 1:
			count += 1
		x = int( x / 2 )
	return count

# Simple tests

print("No. of ones in 0b:",count_ones(0))
print("No. of ones in 1b:",count_ones(1))
print("No. of ones in 2b:",count_ones(2))
print("No. of ones in 3b:",count_ones(3))
print("No. of ones in 4b:",count_ones(4))
print("No. of ones in 5b:",count_ones(5))



