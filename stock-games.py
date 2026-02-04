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
            games = {
                "Game_name": name,
                "Game_price": price,
            }
            stock.update(games)
        save_data()
    if option == 2:
        print("Os Jogos Cadastrados São: ")
        print(stock)
    break