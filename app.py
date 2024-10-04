# dicionário 

usuario = {
        "nome":"Samuel Vitor",
        "idade":"25",
        "Profissão":"Programador",
        "email":"samukalau@gmail.com"

}

# usuário informa novos valores 
usuario["nome"] = input("Informe o nome: ")
usuario["idade"] = int(input("Informe o idade: "))
usuario["profissão"] = input("Informe o profissão: ")
usuario["email"] = input("Informe o email: ")


# exibir o dicionário na tela
# print("DADOS DOS USUÁRIOS:\n")
# print(f"Nome do usuário: {usuario["nome"]}.")
# print(f"Nome do usuário: {usuario["idade"]}.")
# print(f"Nome do usuário: {usuario["Profissão"]}.")
# print(f"Nome do usuário: {usuario["email"]}.")

# exibe os valores do dicionário na tela
print("DADOS DOS USUÁRIOS:\n")
print(f"Nome do usuário: {usuario.get("nome")}")
print(f"Idade do usuário: {usuario.get("idade")}")
print(f"Profissão do usuário: {usuario.get("Profissão")}")
print(f"Email do usuário: {usuario.get("email")}")

