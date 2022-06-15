import math

def gauss_quadrature(xi , xf, n, function):

    roots = list()
    weights = list()

    ## Given roots and weights for Gauss quadrature

    if n == 2:

        roots.append(-0.577350269189626)
        roots.append(0.577350269189626)
        weights.append(1)
        weights.append(1)

    elif n == 4:

        roots.append(-0.861136)
        roots.append(-0.339981)
        roots.append(0.339981)
        roots.append(0.861136)
        weights.append(0.347855)
        weights.append(0.652145)
        weights.append(0.652145)
        weights.append(0.347855)

    elif n == 6:

        roots.append(-0.932470)
        roots.append(-0.661209)
        roots.append(-0.238619)
        roots.append(0.238619)
        roots.append(0.661209)
        roots.append(0.932470)
        weights.append(0.171324)
        weights.append(0.360726)
        weights.append(0.467914)
        weights.append(0.467914)
        weights.append(0.360726)
        weights.append(0.171324)

    else:

        print("Invalid number of points")
        return

    transformed_roots = list()
    for root in roots:
        transformed_roots.append(root * (xf - xi) / 2 + (xi + xf) / 2)
    
    values = list()
    for root in transformed_roots:
        values.append(function(root))
    
    sum = 0

    for i in range(len(values)):
        sum += weights[i] * values[i]
    
    return sum * (xf - xi) / 2