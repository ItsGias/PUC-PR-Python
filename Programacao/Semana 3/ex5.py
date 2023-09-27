#Exercício de fixação 5: Crie um programa que peça dois números ao usuário – o primeiro será o numerador e o segundo, o expoente. A saída do programa deve ser o resultado da operação: numerador elevado ao expoente. Observação: não use a função própria do Python que calcula automaticamente potência.

result = 1
numerator  = int(input("Insert the numerator: "))
exponent   = int(input("Insert the exponent: "))
for i in range(exponent):
    result *= numerator 

print("The result is: %i " % result)