#input years
y = eval(input("Enter the number of years: "))

#pop math
p = int(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * y))

#print pop total
print("The population in 5 years is", p)