nome_usuario = input("Qual é o seu nome? ")

print(f"Bem-vindo ao Clube de Magia de Hogwarts, {nome_usuario}!\n")
print("Aqui você pode criar sua lista de desejos de itens e experiências mágicas!\n")

NOME_ARQUIVO = f"{nome_usuario}_desejos_harry_potter.txt"
desejos = []

try:
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            desejos.append(linha.strip())
    print(f"Seus desejos foram carregados do arquivo '{NOME_ARQUIVO}'\n")
except FileNotFoundError:
    print("Parece que é sua primeira vez no Clube de Magia! Vamos criar sua lista de desejos.\n")
except Exception as e:
    print(f"Ocorreu um erro ao carregar os desejos: {e}")

def salvar_desejos(lista_de_desejos):
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for desejo in lista_de_desejos:
                arquivo.write(desejo + "\n")
        print("\nSeus desejos foram salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os desejos: {e}")

while True:
    print("\n--- O que você quer fazer? ---")
    print("1 - Adicionar um novo desejo de item mágico")
    print("2 - Adicionar um novo desejo de experiência mágica")
    print("3 - Ver meus desejos")
    print("4 - Sair")
    opcao = input("Digite sua opção (1, 2, 3 ou 4): ")

    if opcao == "1":
        novo_desejo = input("Qual é o item mágico que você deseja? (Ex: Varinha de Voldemort, Capa de Invisibilidade) ")
        if novo_desejo.strip():
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos)
        else:
            print("Desejo não pode ser vazio! Tente novamente.")
    elif opcao == "2":
        novo_desejo = input("Qual é a experiência mágica que você deseja? (Ex: Voar em uma vassoura, Visitar o Castelo de Hogwarts) ")
        if novo_desejo.strip():
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos)
        else:
            print("Desejo não pode ser vazio! Tente novamente.")
    elif opcao == "3":
        print("\nMeus Desejos de Harry Potter")
        if not desejos:
            print("Ainda não há desejos na sua lista. Que tal adicionar um?")
        else:
            for i, desejo in enumerate(desejos):
                print(f"{i+1}. {desejo}")
            print("--------------------------")
    elif opcao == "4":
        print("Até a próxima! Continue sonhando com o mundo mágico de Harry Potter!")
        break
    else:
        print("Opção inválida. Por favor digite 1, 2, 3 ou 4.")
