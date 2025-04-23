import sqlite3
import os
con = sqlite3.connect('produtos.db')
cur = con.cursor()


def adicionar_produto(nome_produto, quantidade_produto, preco_produto_unidade, preco_produto_total):
    cur.execute("CREATE IF NOT EXISTS produtos(nome, quantidade, preco, preco_total")
    cur.execute("INSERT INTO ")



def criar_tabela(nome_produto_tabela, quantidade_produto_tabela):
      print(f"{'-='*25}")
      print("Fruta\t \tQuantidade")
      print(f"{nome_produto_tabela} \t{quantidade_produto_tabela}")



Estoque = {}
while True:


      print(f'{20*'-='}')
      print(f"{10* ' '}Escolha uma opção")
      print(f'{20*'-='}')
      escolhaMenu = int(input(' 1 - Adicionar produto \n 2 - Remover produtos \n 3 - Ver produtos'
            '\n 4 - Sair do programa'))


      if escolhaMenu == 1:
            while True:
                  print(f'{20 * '-='}')
                  print(f"{10 * ' '}Escolha uma opção")
                  print(f'{20 * '-='}')
                  opcao_escolha1 = int(input(' 1 - Adicionar um produto \n 2 - Sair para o menu'))
                  if opcao_escolha1 == 1:
                        nome = str(input('Digite o nome do produto: '))
                        try:
                              quantidade = int(input('Digite a quantidade do produto: '))
                              adicionar_produtos(Estoque, quantidade, nome)
                        except ValueError:
                              print("Digite uma quantidade válida.")
