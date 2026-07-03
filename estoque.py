import sqlite3

def clear_screen():
    import os
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()


conexao = sqlite3.connect("Database/estoque.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT UNIQUE NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
    )
    """)

conexao.commit()

while True:
    print("""
    1 - Cadastrar Produto
    2 - Remover Produto
    3 - Remover Quantidade
    4 - Adicionar Quantidade
    5 - Exibir Produtos
    6 - Sair
    """)
    print("-" * 20)

    try:
        opcao = int(input("Opção: "))

        # CADASTRAR PRODUTO
        if opcao == 1:
            print("-" * 20)

            produto = input("Produto: ").capitalize()
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))

            try:
                cursor.execute("""
                    INSERT INTO estoque (produto, preco, quantidade)
                    VALUES (?, ?, ?)
                """, (produto, preco, estoque))

                conexao.commit()

                print("Produto cadastrado!")
                print("-" * 20)

            except sqlite3.IntegrityError:
                print("Produto já existe!")
                print("-" * 20)

        # REMOVER PRODUTO
        elif opcao == 2:
            print("-" * 20)

            remover = input("Qual produto deseja remover: ").capitalize()

            cursor.execute(
                "SELECT * FROM estoque WHERE produto = ?",
                (remover,)
            )

            produto_encontrado = cursor.fetchone()

            if produto_encontrado:
                cursor.execute(
                    "DELETE FROM estoque WHERE produto = ?",
                    (remover,)
                )

                conexao.commit()

                print("Produto removido!")
            else:
                print("Produto não encontrado.")

            print("-" * 20)

        # REMOVER QUANTIDADE
        elif opcao == 3:
            print("-" * 20)

            remover_estoque = input("Qual produto deseja alterar? ").capitalize()

            cursor.execute("""
                SELECT quantidade
                FROM estoque
                WHERE produto = ?
            """, (remover_estoque,))

            resultado = cursor.fetchone()

            if resultado:
                estoque_atual = resultado[0]

                quantidade = int(input("Quantidade a remover: "))

                if quantidade <= estoque_atual:
                    novo_estoque = estoque_atual - quantidade

                    cursor.execute("""
                        UPDATE estoque
                        SET quantidade = ?
                        WHERE produto = ?
                    """, (
                        novo_estoque,
                        remover_estoque
                    ))

                    conexao.commit()

                    print("Estoque atualizado!")
                else:
                    print("Quantidade maior que o estoque disponível.")
            else:
                print("Produto não encontrado.")

            print("-" * 20)

        # ADICIONAR QUANTIDADE
        elif opcao == 4:
            print("-" * 20)

            add_estoque = input("Qual produto deseja alterar? ").capitalize()

            cursor.execute("""
                SELECT quantidade
                FROM estoque
                WHERE produto = ?
            """, (add_estoque,))

            resultado = cursor.fetchone()

            if resultado:
                estoque_atual = resultado[0]

                quantidade = int(input("Quantidade a adicionar: "))

                novo_estoque = (estoque_atual + quantidade)

                cursor.execute("""
                    UPDATE estoque
                    SET quantidade = ?
                    WHERE produto = ?
                """, (novo_estoque,
                    add_estoque))

                conexao.commit()

                print("Estoque atualizado!")
            else:
                print("Produto não encontrado.")

            print("-" * 20)

        # EXIBIR PRODUTOS
        elif opcao == 5:
            print("-" * 20)

            cursor.execute("""
                SELECT produto, preco, quantidade
                FROM estoque
            """)

            produtos = cursor.fetchall()

            if produtos:
                for produto in produtos:
                    print(f"Produto: {produto[0]}")
                    print(f"Preço: R${produto[1]:.2f}")
                    print(f"Estoque: {produto[2]}")
                    print("-" * 20)
            else:
                print("Nenhum produto cadastrado.")
                print("-" * 20)

        # SAIR
        elif opcao == 6:
            print("-" * 20)
            print("Saindo...")
            break

        else:
            print("-" * 20)
            print("ERRO! Opção inválida")
            print("-" * 20)

    except ValueError:
        print("Opção só pode ser números")
        print("-" * 20)

# Fechar conexão
conexao.close()
