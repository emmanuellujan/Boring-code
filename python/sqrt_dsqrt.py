# This function calculates the squared root of a number through the fixed point
# method. At the same time it also it calculates the derivative of the squared root.

def sqrt_dsqrt(x, n=100):
    y = x / 2
    dy = 1 / 2
    for i in range(n):
        #y = x / y # This scheme oscilates
        #y = y + x - y * y # This scheme oscilates or diverges
        y = 0.5 * ( y + x / y ) # This scheme converges
        dy = 0.5 * ( dy + ( y - x * dy ) / y**2 )
    return y, dy

# Simple tests

print( "sqrt(x), dsqrt(x)/dx")
print( " when x = 2 :", sqrt_dsqrt(2) )
print( " when x = 49 :", sqrt_dsqrt(49) )


