#input asking for the a-f inputs
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

#if statement checking for solution
if a * d - b * c == 0:

    print("The equation has no solution")

else:

    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
#printing result of x and y 
    print("x is", format(x, "0.1f"), "y is", format(y, "0.1f"))