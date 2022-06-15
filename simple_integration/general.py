from trapezoids import trapezoid
from simpson1_3 import simpson1_3
from simpson3_8 import simpson3_8

import math

def function(x):
    return x**2/2

xi = 0
xf = 3
n = 2000

trapezoid_result = round(trapezoid(xi, xf, n, function), 6)
simpson1_3_result = round(simpson1_3(xi, xf, n, function), 6)
simpson3_8_result = round(simpson3_8(xi, xf, n, function), 6)

print(f"\nTrapezoid = {trapezoid_result}")
print(f"Simpson 1/3 = {simpson1_3_result}")
print(f"Simpson 3/8 = {simpson3_8_result}\n")
