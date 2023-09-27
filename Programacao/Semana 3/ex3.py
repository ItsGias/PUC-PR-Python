#Exercício de fixação 3: Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes, removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos.

phrase = str(input("Please insert a phrase: "))
consonant = ""

for letter in phrase:
     if letter.lower() not in "aeiou":
        consonant = consonant + letter

print("The phrase without vogals is: %s " % consonant)