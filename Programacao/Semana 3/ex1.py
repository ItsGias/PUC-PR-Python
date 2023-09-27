#Exercício de fixação 1: Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final essas informações.

even = 0
odd = 0

for i in range(1,11):
    num = int(input("Insert the number %d: "% i))
    if (num % 2) == 0:
        even += 1
    else:
        odd += 1

print("\n1You inserted %i even numbers and %i odd numbers" % (even, odd))