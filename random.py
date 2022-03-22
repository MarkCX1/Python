#importing random number
import random

n1, n2 = random.randint(0, 99), random.randint(0, 99)
#Set of strings asking for an input
s = "What is " + str(n1) + " * " + str(n2) + " ? "
res = eval(input(s))

if res == (n1 * n2):
    #if statement checking if the res is correct
    print("You are correct!")
else:
    #else statement rerouting the code to run this code instead
    print("You are wrong")
    print(str(n1), "*", str(n2), "=", str(n1 * n2))