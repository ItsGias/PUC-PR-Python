'''
File: Atividade Somativa 2.py

Author: Gian Lucas dos Reis (gianlucas.reis@gmail.com)

Course: Gestão da tecnologia da informação

Class: Raciocínio computacional

brief: Atividade Somativa 2 do projeto de disciplina de Raciocínio computacional

Date: 24-09-2023
'''


import json

mainOption = 0 #Variable to use at the main menu inside the While function
studentList = [] #Pre determines the array that will be created for the students list
teacherList = [] #Pre determines the array that will be created for the teachers list
disciplineList = [] #Pre determines the array that will be created for the discipline list
registrationList = [] #Pre determines the array that will be created for the registrations list
classList = [] #Pre determines the array that will be created for the class list
saveFileList = [] #Pre determines the array that will be created for the save file list



def saveAllListsToJson():
    saveFileList = {
        "students": studentList,
        "teachers": teacherList,
        "disciplines": disciplineList,
        "registrations": registrationList,
        "classes": classList
    }
    with open("fileList.json", "w", encoding="utf-8") as file:
        json.dump(saveFileList, file, ensure_ascii=False)
        file.close()
# Function to save all the data at the file

def loadDataFromJson():
    try:
        file_path = "fileList.json"
        with open(file_path, "r", encoding="utf-8") as file:
            allLists = json.load(file)
            print("File founded, loading all the previously saved data...")
            # Load data into your global lists
            studentList.extend(allLists["students"])
            teacherList.extend(allLists["teachers"])
            disciplineList.extend(allLists["disciplines"])
            registrationList.extend(allLists["registrations"])
            classList.extend(allLists["classes"])
    except FileNotFoundError:
        print("File not found\n")
        # Handle the case where the file does not exist
        pass
# Function to load data from the JSON file

def mainMenu():
    print("\n----- MAIN MENU -----")
    print("")
    print("(1) Manage Students.")
    print("(2) Manage Disciplines.")
    print("(3) Manage Teachers.")
    print("(4) Manage Classes.")
    print("(5) Manage registration.")
    print("(9) Exit.")
    return int(input("\nChoose an option: "))
#Main menu function

def insideMenu(userChoice):
        print("")
        print("[%s'S] OPERATIONS MENU:" %userChoice)
        print("(1) Include.")
        print("(2) List.")
        print("(3) Update.")
        print("(4) delete")
        print("(9) Go back to the main menu.")
        print("")
        return int(input("Insert the desired option: "))
#Menu function for every option

def insideInclusion(userChoice):
    print("\n===== INCLUSION =====\n")
    if userChoice == "class":
        userChoiceCode = int(input("Enter %s' code: "% userChoice))
        userChoiceTeacher = int(input("Enter the teacher code: "))
        userChoiceDiscipline = int(input("Enter the discipline code: "))

        isChoiceCodeTaken = any(classData["ClassCode"] == userChoiceCode for classData in classList)
        if isChoiceCodeTaken:
            print("\nThe Class code %i is already taken!!!\n" % userChoiceName)
        else:
            isChoiceTeacherTaken = any(classData["TeacherCode"] == userChoiceCode for classData in classList)
            if isChoiceTeacherTaken:
                print("\nThe Teacher code %i is already taken!!!\n" % userChoiceTeacher)
            else:
                isChoiceDisciplineTaken = any(classData["Cpf"] == userChoiceCpf for classData in classList)
                if isChoiceDisciplineTaken:
                    print("\nThe Discipline code %i is already taken!!!\n" % userChoiceDiscipline)
                else:
                    
                 classData = {"ClassCode": userChoiceCode, "TeacherCode": userChoiceTeacher, "DisciplineCode": userChoiceDiscipline}
                 classList.append(classData)
    #for the Class option
    
    elif userChoice == "registration":
        userChoiceClass = int(input("Enter Class' code: "))
        userChoiceStudent = int(input("Enter student's code: "))
        
        isClassCodeTaken = any(registrationData["ClassCode"] == userChoiceClass for registrationData in registrationList)
        if isClassCodeTaken:
                print("\nThe class code %i is already taken!!!\n" % userChoiceClass)
        else:
                isChoiceStudent = any(registrationData["StudentCode"] == userChoiceStudent for registrationData in registrationList)
                if isChoiceStudent:
                    print("\nThe student code %i is already taken!!!\n" % userChoiceStudent) 
                else:
                    registrationData = {"ClassCode": userChoiceClass, "StudentCode": userChoiceStudent}
                    registrationList.append(registrationData)
        
    #for the Registrations option
   
    else:
        userChoiceName = str(input("Please enter the name of the %s: "% userChoice))
        userChoiceCode = int(input("Enter %s's code: "% userChoiceName))
        if userChoice == "teacher" or userChoice == "student":
            userChoiceCpf = str(input("Enter %s's cpf: "% userChoiceName))
        #Gets the CPF if it's a student or a teacher

        if userChoice == "student":
            isNameTaken = any(studentData["Name"] == userChoiceName for studentData in studentList)
            if isNameTaken:
                print("\nThe name %s is already taken!!!\n" % userChoiceName)
            else:
                isCodeTaken = any(studentData["Code"] == userChoiceCode for studentData in studentList)
                if isCodeTaken:
                    print("\nThe code %i is already taken!!!\n" % userChoiceCode)
                else:
                    isCpfTaken = any(studentData["Cpf"] == userChoiceCpf for studentData in studentList)
                    if isCpfTaken:
                        print("\nThe CPF %s is already taken!!!\n" % userChoiceCpf)
                    else:
                        studentData = {"Name": userChoiceName, "Code": userChoiceCode, "Cpf": userChoiceCpf}
                        studentList.append(studentData)
        #Checks if the user repeated the same name, Cpf or code. Then gets the data

        elif userChoice == "teacher":
            isNameTaken = any(teacherData["Name"] == userChoiceName for teacherData in teacherList)
            if isNameTaken:
                print("\nThe name %s is already taken!!!\n" % userChoiceName)
            else:
                isCodeTaken = any(teacherData["Code"] == userChoiceCode for teacherData in teacherList)
                if isCodeTaken:
                    print("\nThe code %i is already taken!!!\n" % userChoiceCode)
                else:
                    isCpfTaken = any(teacherData["Cpf"] == userChoiceCpf for teacherData in teacherList)
                    if isCpfTaken:
                        print("\nThe CPF %s is already taken!!!\n" % userChoiceCpf)
                    else:
                        teacherData = {"Name": userChoiceName, "Code": userChoiceCode, "Cpf": userChoiceCpf}
                        teacherList.append(teacherData)
        #Checks if the user repeated the same name, Cpf or code. Then gets the data

        elif userChoice == "discipline":
            isNameTaken = any(disciplineData["Name"] == userChoiceName for disciplineData in disciplineList)
            if isNameTaken:
                print("\nThe name %s is already taken!!!\n" % userChoiceName)
            else:
                isCodeTaken = any(disciplineData["Code"] == userChoiceCode for disciplineData in disciplineList)
                if isCodeTaken:
                    print("\nThe code %i is already taken!!!\n" % userChoiceCode) 
                else:
                    disciplineData = {"Name": userChoiceName, "Code": userChoiceCode}
                    disciplineList.append(disciplineData)
        #Checks if the user repeated the same name or code. Then gets the data
    #for Student, Teacher and Discipline option
       
    print("Press ENTER to continue...")
    input("")
#Inclusion menu Function

def insideLists(data, userChoiceList, name):
    if len(userChoiceList) == 0:
        print("\nThere are no %s registered.\n" % name)
                #Function to tell the user that there are any %s registered
    else: 
        print("\n===== LISTING =====\n")                
        if userChoiceList == classList:
            for data in userChoiceList:
                print("Class code: ", data["ClassCode"])
                print("Teacher's code: ", data["TeacherCode"])
                print("Discipline's code: ", data["DisciplineCode"])
                print("")  # Add an empty line
        #for the Class option
        
        elif userChoiceList == registrationList:
            for data in userChoiceList:
                print("Class code: ", data["ClassCode"])
                print("Student's code: ", data["StudentCode"])
                print("")  # Add an empty line
        #for the Registrations option
       
        elif userChoiceList == teacherList or userChoiceList == studentList or userChoiceList == disciplineList:
            for data in userChoiceList:
                print("Name: ", data["Name"])
                print("Code: ", data["Code"])
                if name == "students" or name == "teachers":
                    print("Cpf: ", data["Cpf"])
                print("")  # Add an empty line
        #for Student, Teacher and Discipline option
    print("Press ENTER to continue...")
    input("")
# Function to show the list of the desired option that were included in the list 

def insideUpdates(data, userChoiceList, name):
    print("\n===== UPDATING =====\n")
    
    if userChoiceList == classList:
        update = int(input("Enter the code of the %s that you want to update: " % name))
        for data in userChoiceList:
            if update == data["ClassCode"]:
                data["ClassCode"] = str(input("Enter the new Class code: "))
                data["TeacherCode"] = int(input("Enter the new Teacher's code: "))
                data["DisciplineCode"] = int(input("Enter the new Discipline's code: "))
            break

    elif userChoiceList == registrationList:
        update = int(input("Enter the code of the student that you want to update the registration: "))
        for data in userChoiceList:
            if update == data["StudentCode"]:
                data["ClassCode"] = str(input("Enter the new Class code: "))
                data["StudentCode"] = int(input("Enter the new Student's code: "))
            break

    elif userChoiceList == teacherList or userChoiceList == studentList or userChoiceList == disciplineList:
        update = int(input("Enter the code of the %s that you want to update: " % name))
        for data in userChoiceList:
            if update == data["Code"]:
                data["Name"] = str(input("Enter the new name: "))
                data["Code"] = int(input("Enter the new code: "))
                if name == "student" or name == "teacher":    
                    data["Cpf"] = str(input("Enter the new cpf: "))
            break
    print("Press ENTER to continue...")
    input("")
# Function to update the data of the desired               

def insideDelete(data, userChoiceList, name):    
    print("\n===== DELETING =====\n")
    
    if userChoiceList == classList:
        exclusion = int(input("Enter the code of the %s that you want to exclude: "% name))
        for data in userChoiceList:
            if exclusion == data["ClassCode"]:
                print("\nDeleting the data from Class code %i ...\n"% data["ClassCode"])
                userChoiceList.remove(data)
                break
    
    elif userChoiceList == registrationList:
         exclusion = int(input("Enter the code of the student that you want to exclude the registration: "))
         for data in userChoiceList:
            if exclusion == data["StudentCode"]:
                print("\nDeleting Registration data from student's code %i ...\n"% (data["StudentCode"]))
                userChoiceList.remove(data)
                break

    elif userChoiceList == teacherList or userChoiceList == studentList or userChoiceList == disciplineList:
        exclusion = int(input("Enter the code of the %s that you want to exclude: "% name))
        for data in userChoiceList:
            if exclusion == data["Code"]:
                print("\nDeleting the data from %s's code %i ...\n"% (name, data["Code"]))
                userChoiceList.remove(data)
                break
    print("Press ENTER to continue...")
    input("")            
# Function to delete the desired data
    

loadDataFromJson()
# Call the function to load data from the JSON file at the beginning of software

while True:
#Loop through the the entire menu until someone presses " 9 "
    try:        
        
        mainOption = mainMenu()
        #Main Menu function call
        if mainOption == 9:
            print("")
            break
        #Exits the loop

        if mainOption == 1:
            operationsOption = insideMenu("STUDENT")
            try:
                if operationsOption == 1:
                    insideInclusion("student")
                # Calls function to include the student data at the list
                if operationsOption == 2:
                    insideLists("studentData", studentList, "students")
                # Calls function that shows the student data list    
                if  operationsOption == 3:
                    insideUpdates("studentData", studentList, "student")
                # Calls function that updates a student data at the list
                if  operationsOption == 4:
                    insideDelete("studentData", studentList, "student")
                # Calls function that deletes a student data of the list
                if operationsOption == 9:
                    print("Okay, going back to the main menu!!!")
                # Goes back to the main menu
                else:
                    print("Invalid Number, please try again!!!")
                # Checks if the user inserted a correct value
            except ValueError:
                print("\nPlease, insert a correct value!!!!")
    # Except for value error, showing the user what he did wrong
        #Students Menu            

        if  mainOption == 2:
            try:
                operationsOption = insideMenu("DISCIPLINE")
                if operationsOption == 1:
                    insideInclusion("discipline")
                # Calls function to include the discipline data at the list
                if operationsOption == 2:
                    insideLists("disciplineData", disciplineList, "disciplines")
                # Calls function that shows the discipline data list    
                if  operationsOption == 3:
                    insideUpdates("disciplineData", disciplineList, "discipline")
                # Calls function that updates a discipline data at the list
                if  operationsOption == 4:
                    insideDelete("disciplineData", disciplineList, "discipline")
                # Calls function that deletes a discipline data of the list
                if operationsOption == 9:
                    print("Okay, going back to the main menu!!!")
                # Goes back to the main menu
                else:
                    print("Invalid Number, please try again!!!")
                # Checks if the user inserted a correct value
            except ValueError:
                print("\nPlease, insert a correct value!!!!")
    # Except for value error, showing the user what he did wrong
        #disciplines Menu
        
        if  mainOption == 3:
            try:
                operationsOption = insideMenu("TEACHER")
                if operationsOption == 1:
                    insideInclusion("teacher")
                # Calls function to include the teacher data at the list
                if operationsOption == 2:
                    insideLists("teacherData", teacherList, "teachers")
                # Calls function that shows the teacher data list    
                if  operationsOption == 3:
                    insideUpdates("teacherData", teacherList, "teacher")
                # Calls function that updates a teacher data at the list
                if  operationsOption == 4:
                    insideDelete("teacherData", teacherList, "teacher")
                # Calls function that deletes a teacher data of the list
                if operationsOption == 9:
                    print("Okay, going back to the main menu!!!")
                # Goes back to the main menu
                else:
                    print("Invalid Number, please try again!!!")
                # Checks if the user inserted a correct value
            except ValueError:
                print("\nPlease, insert a correct value!!!!")            
        #teachers Menu  

        if  mainOption == 4:
            try:
                operationsOption = insideMenu("CLASSES")
                if operationsOption == 1:
                    insideInclusion("class")
                # Calls function to include the teacher data at the list
                if operationsOption == 2:
                    insideLists("classData", classList, "class")
                # Calls function that shows the teacher data list    
                if  operationsOption == 3:
                    insideUpdates("classData", classList, "class")
                # Calls function that updates a teacher data at the list
                if  operationsOption == 4:
                    insideDelete("classData", classList, "class")
                # Calls function that deletes a class data of the list
                if operationsOption == 9:
                    print("Okay, going back to the main menu!!!")
                # Goes back to the main menu
                else:
                    print("Invalid Number, please try again!!!")
                # Checks if the user inserted a correct value
            except ValueError:
                print("\nPlease, insert a correct value!!!!")
        #classes Menu

        if  mainOption == 5:
            try:
                operationsOption = insideMenu("REGISTRATION")
                if operationsOption == 1:
                    insideInclusion("registration")
                # Calls function to include the teacher data at the list
                if operationsOption == 2:
                    insideLists("registrationData", registrationList, "registration")
                # Calls function that shows the teacher data list    
                if  operationsOption == 3:
                    insideUpdates("registrationData", registrationList, "registration")
                # Calls function that updates a teacher data at the list
                if  operationsOption == 4:
                    insideDelete("registrationData", registrationList, "registration")
                # Calls function that deletes a class data of the list
                if operationsOption == 9:
                    print("Okay, going back to the main menu!!!")
                # Goes back to the main menu
                else:
                    print("Invalid Number, please try again!!!")
                # Checks if the user inserted a correct value
            except ValueError:
                print("\nPlease, insert a correct value!!!!")
        #registration Menu    
                 
    except ValueError:
        print("\nPlease, insert a correct value!!!!")
    # Except for value error, showing the user what he did wrong
       
print("===== Updating =====\n")
saveAllListsToJson()
#Calls the function to update or save the file

print("Closing the software...\n")
#End of the software
