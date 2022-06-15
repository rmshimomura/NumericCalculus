def simpson1_3(xi, xf, n, function):
    h = (xf - xi) / n
    values = []
    for i in range(n + 1):
        values.append(function(xi + h * i))
    coefficients = [1]
    for i in range(1, n):
        if i % 2 == 0:
            coefficients.append(2)
        else:
            coefficients.append(4)
    coefficients.append(1)
    sum = 0
    for i in range(len(values)):
        sum += coefficients[i] * values[i]
    return (sum*h)/3
