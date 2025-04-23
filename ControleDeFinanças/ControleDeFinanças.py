import sqlite3
import os

con = sqlite3.connect('produtos.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS produtos(nome VARCHAR(20), quantidade INTEGER)')



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def adicionar_produtos_db():
    produto_add = str(input("Digite o nome do produto: ")).lower()
    quantidade_produtos = int(input("Digite a quantidade de produtos: "))
    con.execute("INSERT INTO produtos VALUES(?, ?)", (produto_add, quantidade_produtos))
    con.commit()


def remover_produtos_db(produto_rmv, quantidade_rmv):
    con.execute("DELETE FROM produtos WHERE nome = ?", (produto_rmv,))
    con.execute("DELETE FROM produtos WHERE nome = ?", (quantidade_rmv,))
    con.commit()


def listar_produtos_db(produto_db):
    cur.execute("SELECT * FROM produtos WHERE nome = ?", (produto_db,))
    resultado = cur.fetchall()
    if resultado:
        for produto in resultado:
            print(f"Nome: {produto[0]}, Quantidade: {produto[1]}")
    else:
        print("Produto não encontrado.")


while True:
    print(f'{20*"-="}')
    print(f"{10* ' '}Escolha uma opção")
    print(f'{20*"-="}')
    escolhaMenu = int(input(' 1 - Adicionar produto \n 2 - Remover produtos \n 3 - Ver produtos\n 4 - Sair do programa\n→ '))



    if escolhaMenu == 1:
        while True:
            limpar_tela()
            print(f'{20 * "-="}')
            print(f"{10 * ' '}Escolha uma opção")
            print(f'{20 * "-="}')
            opcao_escolha1 = int(input(' 1 - Adicionar um produto \n 2 - Sair para o menu\n→ '))
            if opcao_escolha1 == 1:
                limpar_tela()
                adicionar_produtos_db()
            elif opcao_escolha1 == 2:
                limpar_tela()
                break

    elif escolhaMenu == 2:
        while True:
            limpar_tela()
            print(f'{20 * "-="}')
            print(f"{10 * ' '}Escolha uma opção")
            print(f'{20 * "-="}')
            opcao_escolha2 = int(input(' 1 - Remover um produto \n 2 - Sair para o menu\n→ '))
            if opcao_escolha2 == 1:
                limpar_tela()
                produto_remover = str(input("Digite o nome do produto: ")).lower().strip()
                quantidade_remover = int(input("Digite a quantidade de produtos: "))
                remover_produtos_db(produto_remover, quantidade_remover)
            elif opcao_escolha2 == 2:
                limpar_tela()
                break

    elif escolhaMenu == 3:
        while True:
            limpar_tela()
            print(f'{20 * "-="}')
            print(f"{10 * ' '}Escolha uma opção")
            print(f'{20 * "-="}')
            opcao_escolha3 = int(input(' 1 - Ver um produto específico \n 2 - Ver todos os produtos \n 3 - Sair\n→ '))
            if opcao_escolha3 == 1:
                limpar_tela()
                nome_produto = input("Digite o nome do produto a buscar: ")
                listar_produtos_db(nome_produto,)
            elif opcao_escolha3 == 2:
                limpar_tela()
                cur.execute("SELECT * FROM produtos")
                produtos = cur.fetchall()
                print("\nProdutos cadastrados:")
                for produto in produtos:
                    print(f"Nome: {produto[0]}, Quantidade: {produto[1]}")
            elif opcao_escolha3 == 3:
                limpar_tela()
                break

    elif escolhaMenu == 4:
        limpar_tela()
        print("Saindo do programa...")
        break

con.commit()
con.close()
