from time import sleep
stock = {}
while True:
    print("<<<<- Stock System ->>>>".center(30))
    print("Escolha uma Opção: ".center(30))
    print("1 -> Adicionar um novo Jogo")
    print("2 -> Listar todos os jogos")
    print("3 -> Vender(Remover)Um jogo pelo nome")
    print("4 -> Sair do programa")

    option = int(input("Digite uma opção: "))
    if option == 1:
    # function that saves the datas.
        def save_data():
            name = str(input("Nome do jogo: "))
            price = int(input("Valor do Jogo: "))
            print('-='*15)
            games = {
                "Game_name": name,
                "Game_price": price,
            }

            stock.update(games)
        save_data()
    elif option == 2:
        print(f"A quantidade de jogos no estoque é de {len(stock)}")
        print("Os Jogos Cadastrados São: ")
        print(stock)
    elif option == 3:
        print(f'Os jogos Cadastrados São: {stock} ')
        print(f'E {option} Será Removido...')
        sleep(1)
        stock.pop("Game_name")
        print(stock)
    elif option == 4:
        print("Finalizando o Programa...")
        sleep(1)
        print("Até Mais... Tchau")
        break