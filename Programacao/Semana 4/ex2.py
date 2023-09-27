#Crie um programa que solicite ao usuário duas listas com cinco elementos cada e, como resultado, crie uma terceira lista que intercale os elementos das anteriores.

list1 = []
list2 = []
intercalated = []

for i in range(5):
    num = int(input("Please enter a number to the array slot[%d] of the list one: " % i))
    num2 = int(input("Please enter a number to the array slot[%d] of the list two: " % i))
    list1.append(num)
    list2.append(num2)

for i in range(5):
    intercalated.append(list1[i])
    intercalated.append(list2[i])

print ("The elements intercalated:", intercalated)



