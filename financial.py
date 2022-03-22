#final account value input
final= eval(input("Enter final account value: "))

#inputs for annual interest and ammount of years. 
annual= eval(input("Enter annual interest rate in percent: ")) / 1200
years= eval(input("Enter number of years:  ")) * 12

#math determining the deposit
deposit = final/(1+annual)**years

#output
print(deposit)