#initial input for mins
m=eval(input("Enter the number of minutes: "))

#defining all the days, years, hours, and mins. 
h = m/60
d = h/24
y = m/60/24//365
t=d-365*y

#printing the output of all the math above ^
print(m," is approximately", y," years and ",t," days")
