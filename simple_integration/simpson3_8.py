def simpson3_8(xi, xf, n, function):
    h = (xf - xi) / n
    values = []
    for i in range(n + 1):
        values.append(function(xi + h * i))
    coefficients = [1]
    for i in range(1, n):
        if i % 3 == 0:
            coefficients.append(2)
        else:
            coefficients.append(3)
    coefficients.append(1)
    coefficients[n//2] = 2
    sum = 0
    for i in range(len(values)):
        sum += coefficients[i] * values[i]
    return (sum*h*3)/8