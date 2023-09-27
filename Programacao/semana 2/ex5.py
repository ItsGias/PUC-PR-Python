print("Hello user!!!\n")

print("Please enter the shift that you work")
print("M - Morning")
print("A - Afternoon")
print("E - Evening")
answer = str(input("Answer: "))

if answer == 'M' or answer == 'm':
    print("Good morning!!!")

elif answer == 'A' or answer == 'a':
    print("Good Afternoon!!!")

elif answer == 'E' or answer == 'e':
    print("Good Evening!!!")

else:
    print("Wrong input!\n")

