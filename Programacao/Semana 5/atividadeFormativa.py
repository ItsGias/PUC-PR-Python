mainOption = 0 #Variable to use at the main menu inside the While function
studentList = [] #Pre determines the array that will be created for the students list

while True:
#Loop through the the entire menu until someone presses " 9 "

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
        #Exits the loop

        if mainOption == 1:
            print("")
            print("[STUDENTS] OPERATIONS MENU:")
            print("(1) Include.")
            print("(2) List.")
            print("(3) Update.")
            print("(4) delete")
            print("(9) Go back to the main menu.")
            print("")
            operationsOption = int(input("Insert the desired option: "))
        #Students Menu
            
            if operationsOption == 1:
                print("\n===== INCLUSION =====\n")
                studentName = str(input("Please enter the name of the student: "))
                studentCpf = str(input("Enter %s's cpf: "% studentName))
                studentCode = int(input("Enter %s's code: "% studentName))
            
                student = {"Name": studentName, "Code": studentCode, "Cpf": studentCpf}
                studentList.append(student)
                    
                print("Press ENTER to continue...")
                input("")
            # Function to include the student data at the list

            if operationsOption == 2:
                if len(studentList) == 0:
                    print("\nThere are no students registered.\n")
                #Function to tell the user that there are any students registered
                else: 
                    print("\n===== LISTING =====\n")                
                    for student in studentList:
                        print("Name: ", student["Name"])
                        print("Code: ", student["Code"])
                        print("Cpf: ", student["Cpf"])
                        print("")  # Add an empty line between each student
            # Function to show the list of students that were included in the list
                
                print("Press ENTER to continue...")
                input("")

            if  operationsOption == 3:
                update = int(input("Enter the code of the student that you want to update: "))
                for student in studentList:
                    if update == student["Code"]:
                        student["Name"] = str(input("Enter the new name: "))
                        student["Cpf"] = str(input("Enter the new cpf: "))
                        student["Code"] = int(input("Enter the new code: "))
                        break
            # Function to update the data of the student

            if  operationsOption == 4:
                exclusion = int(input("Enter the code of the student that you want to exclude: "))
                for student in studentList:
                    if exclusion == student["Code"]:
                        studentList.remove(student)
                        break            
            # Function to delete the student data

            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")
            # Goes back to the main menu

        #Students Inclusion Menu

        if  mainOption == 2 or mainOption == 3 or mainOption == 4 or mainOption == 5:
            print("IN DEVELOPMENT PROCESS!\n")
        #Shows to the user that that option hasn't been developed yet

    except ValueError:
        print("\nPlease, insert a correct value!!!!")
    # Except for value error, showing the user what he did wrong
       
print("===== Updating =====\n")

print("Closing the software...\n")
#End of the software
