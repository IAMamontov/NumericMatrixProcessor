import math

x = float(input())
x_rad = math.radians(x)
ctan = math.cos(x_rad) / math.sin(x_rad)
print(round(ctan, 10))
