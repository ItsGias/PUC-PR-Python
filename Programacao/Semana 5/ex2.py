#Exercício de fixação 2: Crie um programa que cadastre os funcionários de uma empresa e seus dependentes. O funcionário deve ser cadastrado com matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla. Dica: use o operador “+=”.

dependents = ""
employee = []

while True:
    if input("Do you want to register an employee and it's dependents? (y/n) ") == "n":
        break
    name = str(input("Please insert a employee name: "))
    registration = int(input("Enter now %s's registration number: " % name))
    data = (name, registration)
 
    while True:
        dependents = input("Please register a %s's dependent: " % name)
        data += (dependents,)
        if input("Do you want to register another dependent? (y/n) ") == "n":
            break
    employee.append(data)

print(employee)
    