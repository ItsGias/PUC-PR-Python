'''
File: Atividade Somativa 1.py

Author: Gian Lucas dos Reis (gianlucas.reis@gmail.com)

Course: Gestão da tecnologia da informação

Class: Raciocínio computacional

brief: Atividade Somativa 1 do projeto de disciplina de Raciocínio computacional

Date: 06-09-2023
'''

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
            operationsOption = int(input("Insert the wished option: "))
        #Students Menu
            
            if operationsOption == 1:
                print("\n===== INCLUSION =====\n")
                studentName = str(input("Please enter the name of the student: "))
                studentList.append(studentName)
                print("Press ENTER to continue...")
                input("")
            #Students Inclusion Menu

            if operationsOption == 2:
                if len(studentList) == 0:
                    print("\nThere are no students registrated.\n")
                #Function to tell the user that there are any students registred
                else: 
                    print("\n===== LISTING =====\n")                    
                    for i in range(len(studentList)):
                        print("- %s" % studentList[i])
                # Function to show the list of students that were included in the list
                
                print("Press ENTER to continue...")
                input("")

            if  operationsOption == 3 or operationsOption == 4:
                print("IN DEVELOPMENT PROCESS!\n")
            #Shows to the user that that option hasn't been developped yet
            
            if operationsOption == "9":
                print("Okay, going back to the main menu!!!")

        if  mainOption == 2 or mainOption == 3 or mainOption == 4 or mainOption == 5:
            print("IN DEVELOPMENT PROCESS!\n")
        #Shows to the user that that option hasn't been developped yet

    except ValueError:
        print("\nPlease, insert a correct value!!!!")
    # Except for value error, showing the user what he did wrong
       
print("===== Updating =====\n")

print("Closing the software...\n")
#End of the software
