'''
Exercício de fixação 4: Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10, no formato:

Tabuada do n

n x 1 = n

n x 2 = 2n

...

n x 10 = 10n
'''

number = int(input("Please insert a number: "))
result = 0

for i in range(1, 11):
    result = number * i
    print ("%i x %i = %i\n" % (i, number, result))