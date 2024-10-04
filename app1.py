# tupla 
campos = ("Nome", "Idade", "Profissão", "E-mail")

# dicionário 1 
# usuario = {
#    campos[0]:"Samuel Vitor",
#    campos[1]:"25",
#    campos[2]:"Estudante",
#    campos[3]:"samuka@gmail.com"
#}

# dicionário 2 
usuario = {}

# entrada de dados 
for campo in campos:
    usuario[campo] = input(f"Informe o valor do campo {campo}: ")
 

# exibe os valores do dicionáriio na tela 
print("DADOS DO USUÁRIO:\n")
for campo in campos:
    print(f"{campo}: {usuario.get(campo)}.")


