agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[contato] = telefone
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break
print(agenda)