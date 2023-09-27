#Exercício de fixação 6: Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações. Caso contrário, exibir a mensagem "Bem-vindo ao sistema!"

while True:

    login,password = str(input("Insert your username and password:")).split(" ")

    if login == password:
        print ("The password can't be the sama as your username, please do it again.\n")

    else:
        print ("\nWelcome to the system!!!!")
        break

