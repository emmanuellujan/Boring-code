# Sum digits of a natural number. E.g. n = 56, sum_digits(56) = 11

def sum_digits(n):
	if n < 10:
		return n
	else:
		return  ( n % 10 ) + sum_digits( int( n / 10 ) ) 

# Simple tests

print("sum_digits(3):", sum_digits(3))
print("sum_digits(56):", sum_digits(56))
print("sum_digits(11111):", sum_digits(11111))
print("sum_digits(12345):", sum_digits(12345))

