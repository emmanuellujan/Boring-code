# Multiplying a number by a binary periodic number
import struct

def float_to_bin(num):
    bits, = struct.unpack('!I', struct.pack('!f', num))
    return "{:032b}".format(bits)

x = 10.0
y = 0.1
if x * y == 1.0:
    print("Good!")
else:
    print("Bad!")

print("IEEE754, 32 bits (1 bit sign, 8 bit exponent, 23 bit mantisa)")
print("x =" , x, "\t its codification is ", float_to_bin(x))
print("y =" , y, "\t its codification is ", float_to_bin(y))
print("x*y =" , x * y, "\t its codification is ", float_to_bin(x*y))
print(1.0, "\t\t its codification is ", float_to_bin(1.0))
print(" " , 1, "\t\t its codification is ", float_to_bin(1))
