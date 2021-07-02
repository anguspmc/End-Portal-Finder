from math import radians, tan
from sympy.solvers import solve
from sympy import Symbol
pos1 = input("Position 1: ").split()
angle1 = float(input("Angle 1: "))
pos2 = input("Position 2: ").split()
angle2 = float(input("Angle 2: "))

angle1 = tan(radians(90 - angle1))
angle2 = tan(radians(90 - angle2))

x1 = 0 - int(pos1[0])
z1 = int(pos1[1])
x2 = 0 - int(pos2[0])
z2 = int(pos2[1])

x, y = Symbol('x y')
print(str(solve(angle1 * (x - x1) + z1 - y == angle2 * (x - x2) + z2 - y)))