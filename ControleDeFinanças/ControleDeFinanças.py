import sqlite3
from os import system, name

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
        preço_total FLOAT,
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    )
''')

cur.excecute('''
    CREATE TABLE IF NOT EXISTS produto_final(
        produto_final_id INTEGER PRIMARY KEY,
        nome_produto_final VARCHAR(20),
        quantidade INTEGER,
        preço FLOAT                
    )         
''')



con.commit()



def limpar_tela():
    system('cls' if name == 'nt' else 'clear')



def definir_preco_total():
    cur.execute("SELECT quantidade FROM ")



def calcular_produto_final(): #precisa mudar o esquema do menu, tornar um menu duplo, uma parte para os produtos brutos e outra parte para o produto final
    #bom deixar um espaço separado p/ o menu de estatística tbm
    produto_utilizado = str(input("Digite o produto usado: "))
    cur.execute("SELECT * FROM produtos WHERE nome = ?", (produto_utilizado)
    resultado_produto_utilizado = cur.fetchall()
    
    if not resultado_produto_utilizado:
        input(f"{produto_utilizado} não encontrado no banco de dados, tente novamente.") 
    else:
        id_produto_utilizado = resultado_produto_utilizado[0]
        quantidade_produtos_utilizado = resultado_produto_utilizado[2]
        
        cur.execute("SELECT * FROM financeiro WHERE produto_id = ?", (id_produto_utilizado))
        resultado_financeiro_id = cur.fetchone()
        preco_produto_utilizado = resultado_financeiro_id[1]

        quantidade_produtos = int(input(f"Digite a quantidade de {produto_utilizado} utilizada"))

        produto_final = str(input("Digite o nome do produto que foi criado: "))
        quantidade_produtos_finais = int(input("Digite a quantidade de produtos finais gerados: "))
        cur.execute("INSERT INTO produto_final (nome_produto_final, quantidade) VALUES (?, ?)", (produto_final, quantidade_produtos_finais))
        
        nova_quantidade_produto_utilizado = quantidade_produtos - quantidade_produtos_utilizado
        if nova_quantidade_produto_utilizado < 0:
            input("Quantidade maior do que a existente no banco de dados. Tente novamente.")
        else:
            cur.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (id_produto_utilizado, nova_quantidade_produto_utilizado))
        preco_final = quantidade_produtos * preco_produto_utilizado / quantidade_produtos_finais


def adicionar_produtos_db():
    produto_add = str(input("Digite o nome do produto: ")).lower()
    quantidade_produtos_add = int(input("Digite a quantidade de produtos: "))
    preco = float(input("Digite o preço unitário do produto: "))
    preco_total = quantidade_produtos_add * preco


    cur.execute('SELECT * FROM produtos WHERE nome = ?', (produto_add,))
    resultado = cur.fetchone()
    

    if not resultado:
        cur.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (produto_add, quantidade_produtos_add))
        produto_last_id = cur.lastrowid
        cur.execute("INSERT INTO financeiro (produto_id, preço_unitario, preço_total) VALUES (?, ?, ?)", (produto_last_id, preco, preco_total))
        con.commit()
        input("✅ Produto novo adicionado com sucesso. \nAperte Enter para continuar...")

    else:
        produto_id = resultado[0]
        quantidade_atual = resultado[2]
        nova_quantidade = quantidade_atual + quantidade_produtos_add
        
        cur.execute("SELECT preço_total FROM financeiro WHERE produto_id = ?", (produto_id,))
        resultado2 = cur.fetchone()
        _=resultado2
        cur.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, produto_id))
        preco_atualizado = resultado2[0] + preco_total
        cur.execute("UPDATE financeiro SET preço_total = ? WHERE produto_id = ?", (preco_atualizado, produto_id,))
        con.commit()
        input("✅ Quantidade atualizada com sucesso. \nAperte Enter para continuar...")



def remover_produtos_db():    
    produto_rmv = str(input("Digite o nome do produto: ")).lower().strip()
    cur.execute("SELECT * FROM produtos WHERE nome = ?", (produto_rmv,))
    resultado = cur.fetchone()
    if not resultado:
        input("Produto não encontrado, tente novamente.")
    else:
        id_produto = resultado[0]
        cur.execute("DELETE FROM produtos WHERE nome = ?", (produto_rmv,))
        cur.execute("DELETE FROM financeiro WHERE produto_id = ?", (id_produto,))
        con.commit()
        input("✅ Produto removido com sucesso. \nAperte Enter para continuar...")


def remover_quantidade():
    produto_rmv = str(input("Digite o nome do produto: ")).lower().strip()
    quantidade_rmv = int(input("Digite a quantidade: "))
    cur.execute("SELECT * FROM produtos WHERE nome = ?", (produto_rmv,))
    resultado = cur.fetchone()
    id_produto_rmvquantidade = resultado[0] 
    if not resultado:
        input("Produto não encontrado, tente novamente.")
    else:
        produto_id = resultado[0]
        quantidade_produto = resultado[2]
        nova_quantidade_produto = quantidade_produto - quantidade_rmv

        if nova_quantidade_produto < 0:
            input("A quantidade digitada é maior do que a disponível em estoque. Tente novamente.")
        else:
            cur.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade_produto, produto_id))
            print(f"A quantidade de {produto_rmv} foi alterada com sucesso! ✅")
            input("Aperte enter para continuar...")

        if nova_quantidade_produto == 0:
            cur.execute("DELETE FROM produtos WHERE nome = ?", (produto_rmv,))
            cur.execute("DELETE FROM financeiro WHERE produto_id = ?", (id_produto_rmvquantidade,))



def listar_produtos_db(produto_db):
    cur.execute("SELECT * FROM produtos WHERE nome = ?", (produto_db,))
    resultado = cur.fetchall()
    if resultado:
        for produto in resultado:
            print(f"Nome: {produto[1]}, Quantidade: {produto[2]}")
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
            escolha_rmv = int(input(' 1 - Remover um produto \n 2 - Alterar a quantidade de um produto\n 3 - Sair '))
            if escolha_rmv == 1:
                limpar_tela()
                remover_produtos_db()
            elif escolha_rmv == 2:
                remover_quantidade()
                limpar_tela()
            elif escolha_rmv == 3:
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
                    print(f"Nome: {produto[1]}, Quantidade: {produto[2]}")
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
