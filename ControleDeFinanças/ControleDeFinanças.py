import sqlite3
import os

con = sqlite3.connect('produtos.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY, 
        nome VARCHAR(20), 
        quantidade INTEGER
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS financeiro (
        produto_id INTEGER, 
        preço_unitario FLOAT, 
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    )
''')
con.commit()
input('teste...')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_produtos_db():
    produto_add = str(input("Digite o nome do produto: ")).lower()
    quantidade_produtos = int(input("Digite a quantidade de produtos: "))
    preco = float(input("Digite o preço unitário do produto: "))

    cur.execute('SELECT * FROM produtos WHERE nome = ?', (produto_add,))
    resultado = cur.fetchone()

    if not resultado:
        cur.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (produto_add, quantidade_produtos))
        produto_last_id = cur.lastrowid
        cur.execute("INSERT INTO financeiro (produto_id, preço_unitario) VALUES (?, ?)", (produto_last_id, preco))
        con.commit()
        input("✅ Produto novo adicionado com sucesso. \nAperte Enter para continuar...")
    else:
        produto_id = resultado[0]
        quantidade_atual = resultado[2]
        nova_quantidade = quantidade_atual + quantidade_produtos
        cur.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, produto_id))
        con.commit()
        input("✅ Quantidade atualizada com sucesso. \nAperte Enter para continuar...")

def remover_produtos_db(produto_rmv):
    cur.execute("DELETE FROM produtos WHERE nome = ?", (produto_rmv,))
    con.commit()

def listar_produtos_db(produto_db):
    cur.execute("SELECT * FROM produtos WHERE nome = ?", (produto_db,))
    resultado = cur.fetchall()
    if resultado:
        for produto in resultado:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}")
    else:
        print("❌ Produto não encontrado.")

while True:
    print(f'{20 * "-="}')
    print(f"{10 * ' '}Escolha uma opção")
    print(f'{20 * "-="}')
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
                remover_produtos_db(produto_remover)
                input("✅ Produto removido com sucesso. \nAperte Enter para continuar...")
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
                nome_produto = input("Digite o nome do produto a buscar: ").lower().strip()
                listar_produtos_db(nome_produto)
                input("\nAperte Enter para continuar...")
            elif opcao_escolha3 == 2:
                limpar_tela()
                cur.execute("SELECT * FROM produtos")
                produtos = cur.fetchall()
                print("\n📦 Produtos cadastrados:")
                for produto in produtos:
                    print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}")
                input("\nAperte Enter para continuar...")
            elif opcao_escolha3 == 3:
                limpar_tela()
                break

    elif escolhaMenu == 4:
        limpar_tela()
        print("👋 Saindo do programa...")
        break

con.commit()
con.close()
