mainOption = 0

while True:

    try:
        print("\n----- MAIN MENU -----")
        print("")
        print("(1) Manage Students.")
        print("(2) Manage Disciplines.")
        print("(3) Manage Teachers.")
        print("(4) Manage Classes.")
        print("(5) Manage registration.")
        print("(9) Exit.")
        mainOption = int(input("\nChoose an option: "))
        if mainOption == 9:
            print("")
            break

        if mainOption == 1:
            print("")
            print("[STUDENTS] OPERATIONS MENU:")
            print("(1) Include.")
            print("(2) List.")
            print("(3) Update.")
            print("(4) delete")
            print("(9) Go back to the main menu.")
            print("")
            operationsOption = input("Insert the wished option: ")
            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")

        if mainOption == 2:
            print("")
            print("[DISCIPLINES] OPERATIONS MENU:")
            print("(1) Include.")
            print("(2) List.")
            print("(3) Update.")
            print("(4) delete")
            print("(9) Go back to the main menu.")
            print("")
            operationsOption = input("Insert the wished option: ")
            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")

        if mainOption == 3:
            print("")
            print("[TEACHERS] OPERATIONS MENU:")
            print("(1) Include.")
            print("(2) List.")
            print("(3) Update.")
            print("(4) delete")
            print("(9) Go back to the main menu.")
            print("")
            operationsOption = input("Insert the wished option: ")
            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")

        if mainOption == 4:
            print("")
            print("[CLASSES] OPERATIONS MENU:")
            print("(1) Include.")
            print("(2) List.")
            print("(3) Update.")
            print("(4) delete")
            print("(9) Go back to the main menu.")
            print("")
            operationsOption = input("Insert the wished option: ")
            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")

        if mainOption == 5:
            print("")
            print("[REGISTRATIONS] OPERATIONS MENU:")
            print("")
            print("(1) Include.")
            print("(2) List.")
            print("(3) Update.")
            print("(4) delete")
            print("(9) Go back to the main menu.")
            print("")
            operationsOption = input("Insert the wished option: ")
            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")
    except ValueError:
        print("\nPlease, insert a correct value!!!!")
       
print("===== Updating =====\n")


print("Closing the software...\n")
