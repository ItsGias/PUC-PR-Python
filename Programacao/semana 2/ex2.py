print("Hello user!!!\n")

creditCardName = str(input("Please enter the name that you want to put on your credit card, remeber that the name can't be bigger than 20 characters: "))

if len(creditCardName) > 20:
    print("\nSorry, but the name that you inserted is too long, please enter a smaller name.\n")

else: print("\nThank you for inserting the name: %s at your's credit card!!!" % creditCardName)