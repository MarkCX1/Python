#importing the math module so we can do math
import math

a, b, c = eval(input("Enter a, b, c "))

discriminant = math.pow(b, 2) - 4 * a * c

if discriminant > 0:

    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    print("The roots are: ", format(r1, "0.6f"), format(r2, "0.6f"))

elif discriminant == 0:
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    print("The root is: ", format(r1, "0.6f"))
else:

    print("No Root")