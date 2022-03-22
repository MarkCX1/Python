import turtle as t

#inputs
x,y = eval(input("Enter the values: "))
rad = eval(input("Enter radius: "))


t.penup()

#setting positions
t.setx(x)
t.sety(y)

#printing the rad
t.write(x*y,align="Center")

#centering
t.sety(y-rad)
t.pendown()

t.circle(rad)
#done
t.done()
