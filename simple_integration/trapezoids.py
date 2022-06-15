def trapezoid(xi, xf, n, function):
    h = (xf - xi) / n
    values = []
    for i in range(n + 1):
        values.append(function(xi + h * i))
    coefficients = [1]
    for i in range(1, n):
        coefficients.append(2)
    coefficients.append(1)
    sum = 0
    for i in range(len(values)):
        sum += coefficients[i] * values[i]
    return (sum*h)/2