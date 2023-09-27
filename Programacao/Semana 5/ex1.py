#Exercício de fixação 1: Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas, adicionando-as a uma lista e imprimindo essa lista no fim do programa.

registration = []
while True:
    name = str(input("Please type a name: "))
    cpf = int(input("Please enter the cpf of %s: " % name ))
    rg = int(input("Please enter the rg of %s: " % name ))

    data = (name, cpf, rg)
    registration.append(data)

    if input("Do you want to continue? (y/n): ") == "n":
        print("\n")
        break

print(registration)