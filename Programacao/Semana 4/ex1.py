#Exercício de fixação 1: Crie um programa que solicite ao usuário seis números, calculando a média, e mostre uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média.

nums = []
result = 0

for i in range(6):
    
    try:
        num = int(input("Please enter a number to the array slot [%i]: " % i))
        nums.append(num)
    except ValueError:
        print ("\nInvalid Number, try again.\n")

for i in range(len(nums)):
    result += nums[i]

print ("\nThe result of all the six numbers inserted is: %d \n" % result)