#Exercício de fixação 2: Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles.

biggestNum = -50000
smallestNum = 50000

for i in range(1,6):
    num = int(input("Please insert the number %i: "%i))
    if num > biggestNum:
        biggestNum = num
    if num < smallestNum:
        smallestNum = num
print("\nThe biggest number is %i and the smallest number is %i\n" % (biggestNum, smallestNum))
    
