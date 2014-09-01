#-*- encoding: utf-8 -*-
tabela = {"Macarrão": 2.30,
  "Batata": 1.20,
  "Feijão": 1.60,
  "Tomate": 2.30}
while True:
    produto = raw_input("Digite o nome do produto ou fim para terminar: ")
    if produto == "fim":
        break
    if produto in tabela:
        print("Preço %.2f" %tabela[produto])
    else:
        print("Produto não encontrado!")
