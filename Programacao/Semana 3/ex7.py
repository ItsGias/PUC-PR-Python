#Exercício de fixação 7: Crie um programa que solicite ao usuário vários números e, ao digitar 0, calcule a média dos números informados.

contador = 0
sum = 0

while True:
    number = int(input("Please insert a number, insert 0 if you want to exit: ")) 
    if number == 0:
        break
    else:
        contador += 1
        sum += number

if contador == 0:
    print ("No numbers were entered!!!")

else:
    average = sum / contador
    print ("The average of the numbers that were entered is: %d" % average)