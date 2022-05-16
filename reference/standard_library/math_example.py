import math

# Factorial
print(math.factorial(5))

# Square Root
print(math.sqrt(7))

# Great Common Divisor
print(math.gcd(21, 14))

# Least Common Multiple
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(lcm(7, 3))

# PI
print(math.pi)

# E
print(math.e)
