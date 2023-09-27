number1= float(input("Please insert the first number: "))
number2= float(input("Please insert the second number: "))

print("Please choose which operation that you want to perform")
operation = str(input("Please enter 'A' for addition, 'B' for multiplication, 'C' for subtraction and 'D' for division: "))

if operation == 'a' or 'A':
    result = number1 + number2
    print("\nThe result of the operation is %.2f\n" % result)
elif operation == 'b' or 'B':
    result = number1 * number2
    print("\nThe result of the operation is %.2f\n" % result)
elif operation == 'c' or 'C':
    result = number1 - number2
    print("\nThe result of the operation is %.2f\n" % result)
elif operation == 'D' or 'd':
    result = number1 / number2
    print("\nThe result of the operation is %.2f\n" % result)
else:
    print("\nWrong input!!!\n")