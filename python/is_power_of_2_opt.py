# Returns if a number x > 0 is power of 2

def is_power_of_2(x):
	return x > 0 and x & (x - 1) == 0

# Simple tests

print("0 is power of 2:",is_power_of_2(0))
print("1 is power of 2:",is_power_of_2(1))
print("2 is power of 2:",is_power_of_2(2))
print("3 is power of 2:",is_power_of_2(3))
print("4 is power of 2:",is_power_of_2(4))
print("7 is power of 2:",is_power_of_2(7))
print("8 is power of 2:",is_power_of_2(8))
print("9 is power of 2:",is_power_of_2(9))

