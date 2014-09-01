#-*- encoding: utf-8 -*-
categoria = input('Informe a categoria do produto: ')
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 20
elif categoria == 3:
    preco = 30
elif categoria == 4:
    preco = 40
else:
    print ('Categoria inválida, informe um valor entre 1 e 4!')
    preco = 0
print ('Preço do produto: R$ %.2f' %preco)
