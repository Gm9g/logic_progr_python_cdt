print("Meus Filmes Favoritos\n")
NOME_ARQUIVO = "meus_filmes.txt"
filmes = []

try:
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            filmes.append(linha.strip())
    print(f"Meus filmes foram carregados do arquivo '{NOME_ARQUIVO}'\n")
except FileNotFoundError:
    print("Parece que é sua primeira vez! Vamos criar sua lista de filmes.\n")
except Exception as e:
    print(f"Ocorreu um erro ao carregar os filmes: {e}")

def salvar_filmes(lista_de_filmes):
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for filme in lista_de_filmes:
                arquivo.write(filme + "\n")
        print("\nSeus filmes foram salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os filmes: {e}")

while True:
    print("\n--- O que você quer fazer? ---")
    print("1 - Adicionar um novo filme")
    print("2 - Ver meus filmes")
    print("3 - Sair")
    print("4 - Pesquisar um filme específico")
    print("5 - Excluir um filme da lista")
    print("6 - Ordenar a lista de filmes")
    opcao = input("Digite sua opção (1, 2, 3, 4, 5 ou 6): ")

    if opcao == "1":
        novo_filme = input("Qual é o seu novo filme favorito? ")
        if novo_filme.strip():
            filmes.append(novo_filme.strip())
            salvar_filmes(filmes)
        else:
            print("Filme não pode ser vazio! Tente novamente.")
    elif opcao == "2":
        print("\nMeus Filmes Favoritos")
        if not filmes:
            print("Ainda não há filmes na sua lista. Que tal adicionar um?")
        else:
            for i, filme in enumerate(filmes):
                print(f"{i+1}. {filme}")
            print("--------------------------")
    elif opcao == "3":
        print("Até a próxima! Continue assistindo filmes incríveis!")
        break
    elif opcao == "4":
        filme_pesquisado = input("Qual filme você deseja pesquisar? ")
        if filme_pesquisado.strip() in filmes:
            print(f"Sim, '{filme_pesquisado}' está na sua lista de filmes!")
        else:
            print(f"Não, '{filme_pesquisado}' não está na sua lista de filmes.")
    elif opcao == "5":
        filme_excluir = input("Qual filme você deseja excluir? ")
        if filme_excluir.strip() in filmes:
            filmes.remove(filme_excluir.strip())
            salvar_filmes(filmes)
            print(f"'{filme_excluir}' foi excluído da sua lista de filmes!")
        else:
            print(f"Não, '{filme_excluir}' não está na sua lista de filmes.")
    elif opcao == "6":
        filmes.sort()
        salvar_filmes(filmes)
        print("A lista de filmes foi ordenada!")
    else:
        print("Opção inválida. Por favor digite 1, 2, 3, 4, 5 ou 6.")
