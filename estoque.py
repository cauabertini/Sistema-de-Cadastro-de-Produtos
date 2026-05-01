produtos = {}

while True:
    print("""
          1-Cadastrar Produto
          2-Remover Produto
          3-Remover Quantidade
          4-Adicionar Quantidade
          5-Exibir Produtos
          6-Sair
          """)
    opcao = int(input("Opcao: "))

    if opcao == 1:
        produto = input("Produto: ")
        preco = float(input("Preco: "))
        estoque = int(input("Estoque: "))
    
        produtos[produto] = {
            "Preço": preco,
            "Estoque": estoque
        }

    elif opcao == 2:
        remover = input("Qual produto deseja remover: ")
        if remover in produtos:
            del produtos[produto]
            print("Produto removido!")
        else:
            print("Produto não encontrado.")
    
    elif opcao == 3:
        remover_estoque = input("Qual produto deseja alterar? ")

        if remover_estoque in produtos:
            quantidade = int(input("Quantidade a remover: "))

            if quantidade <= produtos[produto]["Estoque"]:
                produtos[produto]["Estoque"] -= quantidade
                print("Estoque atualizado!")
            else:
                print("Quantidade maior que o estoque disponível.")
        else:
            print("Produto não encontrado.")
    
    elif opcao == 4:
        add_estoque = input("Qual produto deseja alterar? ")

        if add_estoque in produtos:
            quantidade = int(input("Quantidade a adicionar: "))

            produtos[produto]["Estoque"] += quantidade
            print("Estoque atualizado!")
    
        else:
            print("Produto não encontrado.")



    elif opcao == 5:
        for nome, dados in produtos.items():
            print(f"Produto: {nome}")
            print(f"Preço: R${dados['Preço']}")
            print(f"Estoque: {dados['Estoque']}")
            print("-" * 20)

    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("ERRO! Opcão inválida")