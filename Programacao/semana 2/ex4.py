print("Hello user!!!\n")

salary = float(input("Please insert the amount of money you recieve as yours salary: "))

if salary < 5000:
    allowance = (salary * 15) / 100
    print("Your allowance at the end of the year will be %.2f \n" % (allowance))
else:
    allowance = (salary * 10) / 100
    print("Your allowance at the end of the year will be %.2f \n" % (allowance))