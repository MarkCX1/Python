e1, e2, e3 = eval(input("Enter three edges: "))

#if statement adding 
if e1 + e2 > e3 and e1 + e3 > e2 and e2 + e3 > e1:
    res = e1 + e2 + e3
    #printing perimeter
    print("The perimeter is", str(res))
else:
    #if there is no solution print invalid
    print("The input is invalid")