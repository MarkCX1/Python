#importing math modules
import math


X1 = Y1 = 0
X2 = 0
Y2 = 100
X3 = 200
Y3 = 0
x, y = eval(input("Enter a point's x- and y-coordinates: "))


if x + 2 * y < X3 and 0 <= x <= X3 and 0 <= y <= Y2:
    print("The point is in the triangle ")
else:
    print("The point is not in the triangle ")
