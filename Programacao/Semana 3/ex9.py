#Exercício de fixação 9: Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio), seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo). Ao incluir um produto, deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. Todos os dados devem ser validados. Ao final da compra, deve ser informado o valor total do pedido.

productName = ""
productValue = 0
productAmmount = 0
price = 0
totalAmmount = 0

print ("Hello and welcome to our online supermarket service!!!\n")

while True:
    
    try:
        productName = str(input("\nPlease insert the name of the product: "))
        productValue = float(input("Please insert the value of %s: " %  productName))
        productAmmount = int(input("Type how many %s you want to buy: " %  productName))
        
        price = productValue * productAmmount
        totalAmmount += price

        answer = str(input("Do you want to insert another product? (y/n): "))
        if answer == "y":
             print("Okay, let; insert another product!!!\n")
        else:
             break
    
    except ValueError:
        print("Wrong kind of value inserted!!!")


print("The total amount of your order is %d, thank you for your order!\n" % totalAmmount)

