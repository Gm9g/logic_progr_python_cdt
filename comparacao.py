###Criando uma lista
##Ivan, 
# Tarso, 
# Gustavo
# Gabriel,
# Fabricio,
# Rafael,
# vitor

#Qual seria o print e
#Input para pedir nomes?

print("n\***Lista de Nomes***\n")
nomes = input("Digite os Nomes Separados por Virgula:").split(",")
nomes = [nome.strip() for nome in nomes ]
#print(nomes)

print("\n Quais Operações Você Fazer:")
print("1 - adicionar um nome")
print("2 - Remover um nome")
print("3 - Listar nomes")
print("4 - Sair")

#faça um loop para pedir a opção do usuario
while True:
    

    opcao = input("\n Digite a Opção Desejada (1-4):")

    if opcao == "1":
        #novo_nome = Input("Digite o nome a ser adicionado:")
        #nomes.append(novo_nome)
        #print(f"{novo_nome} foi adicionado à lista)
        print(f"foi adicionado a lista.")
    elif opcao =="3":
        print("\nLista de Nomes:")
        #for_nome