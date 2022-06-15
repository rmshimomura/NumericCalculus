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

real_result = -3.257739

print(f"\nTrapezoid = {trapezoid_result} error = {round(abs(trapezoid_result - real_result), 6)}")
print(f"Simpson 1/3 = {simpson1_3_result} error = {round(abs(simpson1_3_result - real_result), 6)}")
print(f"Simpson 3/8 = {simpson3_8_result} error = {round(abs(simpson3_8_result - real_result), 6)}\n")
