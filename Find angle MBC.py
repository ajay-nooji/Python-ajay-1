import math

AB, BC = int(input()), int(input())
MC = math.sqrt(AB**2 + BC**2) * 0.5
deg = math.degrees(math.atan2(AB, BC))
print("{0}\xb0".format(int(round(deg))))