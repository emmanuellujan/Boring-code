# Returns if a number x is power of y

def is_power_of(x,y):
	while x > 0 and x % y == 0:
		x = x / y
	if x == 1:
		return True
	else:
		return False

# Simple test

print("0 is power of 2:",is_power_of(0,2))
print("1 is power of 2:",is_power_of(1,2))
print("2 is power of 2:",is_power_of(2,2))
print("3 is power of 2:",is_power_of(3,2))
print("4 is power of 2:",is_power_of(4,2))
print("7 is power of 2:",is_power_of(7,2))
print("8 is power of 2:",is_power_of(8,2))
print("9 is power of 2:",is_power_of(9,2))

