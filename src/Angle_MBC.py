# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())

# pythagoras
ac = math.sqrt(pow(ab, 2) + pow(bc, 2))

# AM = MC = MB = radius of circle subtended by ABC (since right triangle)
# therefore BMC isosceles, and theta = arccos(BC/2 * 1/MB) = arccos(BC/AC)
theta = math.acos(bc / ac)

# print theta in degrees, rounded
print("%d°" % round(math.degrees(theta)))