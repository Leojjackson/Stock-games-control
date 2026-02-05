from time import sleep
stock = []


def save_data():
    print('-=' * 15)
    name = str(input("Nome do jogo: "))
    price = float(input("Valor do Jogo: "))
    print('-=' * 15)
    games = {
        "Game_name": name,
        "Game_price": price,
    }
    stock.append(games)
    print(f'Jogo {name} Adicionado com sucesso!')
    print('-=' * 15)

while True:
    print("<<<<- Stock System ->>>>".center(30))
    print("Escolha uma Opção: ".center(30))
    print("1 -> Adicionar um novo Jogo")
    print("2 -> Listar todos os jogos")
    print("3 -> Vender(Remover)Um jogo pelo nome")
    print("4 -> Sair do programa")

    option = int(input("Digite uma opção: "))
    if option == 1:
        save_data()
    elif option == 2:
        print('-=' * 15)
        print(f"A quantidade de jogos no estoque é de {len(stock)}")
        print("Os Jogos Cadastrados São: ")
        for game in stock:
            print(f'Nome: {game['Game_name']} - "Preço: {game["Game_price"]:.2f}"')
        print('-=' * 15)
    elif option == 3:
        search = input("Qual jogo deseja remover? ")
        found = False
        for game in stock:
            if game["Game_name"].lower() == search.lower():
                stock.remove(game)
                print(f'{game["Game_name"]} Removido com sucesso!')
                found = True
                break
        if not found:
            print("Jogo não encontrado")
            print('-=' * 15)
    elif option == 4:
        print("Finalizando o Programa...")
        sleep(1)
        print("Até Mais... Tchau")
        print('-=' * 15)
        break