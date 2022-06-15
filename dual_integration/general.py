from fusion import double_integration

import math

def function(x, y):
    return ((x*y) ** 2)/2

xi = 0
xf = 3
yi = 0
yf = 3
nx = 4
ny = 4

print(double_integration(xi, xf, yi, yf, nx, ny, function, "trapezoid", "simpson1_3"))