# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
c = complex(input())
r = math.sqrt(c.real**2 + c.imag**2)
phi = math.copysign(math.acos(c.real / r), c.imag)
print(r)
print(phi)