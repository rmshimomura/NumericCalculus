def double_integration(xi, xf, yi, yf, nx, ny, function, mode_1, mode_2):

    hx = (xf - xi) / nx
    hy = (yf - yi) / ny

    intervals_x = [xi + hx * i for i in range(nx + 1)]
    intervals_y = [yi + hy * i for i in range(ny + 1)]

    coefficients_x = list()
    coefficients_y = list()

    multiply_x = 0
    multiply_y = 0

    if(mode_1 == "trapezoid"):

        coefficients_x = [1]
        for i in range(1, nx):
            coefficients_x.append(2)
        coefficients_x.append(1)
        multiply_x = 1 / 2

    elif(mode_1 == "simpson1_3"):

        coefficients_x = [1]
        for i in range(1, nx):
            if i % 2 == 0:
                coefficients_x.append(2)
            else:
                coefficients_x.append(4)
        coefficients_x.append(1)
        multiply_x = 1 / 3

    elif(mode_1 == "simpson3_8"):

        coefficients_x = [1]
        for i in range(1, nx):
            if i % 3 == 0:
                coefficients_x.append(2)
            else:
                coefficients_x.append(3)
        coefficients_x.append(1)
        coefficients_x[nx//2] = 2
        multiply_x = 3 / 8

    else:

        print("Invalid mode_1")
        return

    if(mode_2 == "trapezoid"):

        coefficients_y = [1]
        for i in range(1, ny):
            coefficients_y.append(2)
        coefficients_y.append(1)
        multiply_y = 1 / 2

    elif(mode_2 == "simpson1_3"):

        coefficients_y = [1]
        for i in range(1, ny):
            if i % 2 == 0:
                coefficients_y.append(2)
            else:
                coefficients_y.append(4)
        coefficients_y.append(1)
        multiply_y = 1 / 3

    elif(mode_2 == "simpson3_8"):

        coefficients_y = [1]
        for i in range(1, ny):
            if i % 3 == 0:
                coefficients_y.append(2)
            else:
                coefficients_y.append(3)
        coefficients_y.append(1)
        coefficients_y[ny//2] = 2
        multiply_y = 3 / 8

    else:

        print("Invalid mode_2")
        return

    sum_x = 0

    for i in range(len(intervals_x)):
        
        sum_y = 0

        for j in range(len(intervals_y)):
            
            sum_y += function(intervals_x[i], intervals_y[j])* coefficients_y[j]

        sum_y = (sum_y*hy)*multiply_y

        sum_x += sum_y*coefficients_x[i]

    sum_x = (sum_x*hx)*multiply_x

    return sum_x