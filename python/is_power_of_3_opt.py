# Returns if a 32 bit signed integer is power of 3

def is_power_of_3(x):
	return x > 0 and 1162261467 % x == 0


# Simple tests

print("0 is power of 3:",is_power_of_3(0))
print("1 is power of 3:",is_power_of_3(1))
print("3 is power of 2:",is_power_of_3(2))
print("3 is power of 3:",is_power_of_3(3))
print("4 is power of 3:",is_power_of_3(4))
print("7 is power of 3:",is_power_of_3(7))
print("8 is power of 3:",is_power_of_3(8))
print("9 is power of 3:",is_power_of_3(9))
print("3^19 is power of 3:",is_power_of_3(pow(3,19)))


