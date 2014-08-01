#-*- encoding: utf-8 -*-
ultimo = 10
fila = list(range(1,ultimo + 1))
while True:
    print('\nExitem %d clientes na fila' %len(fila))
    print'Fila atual:', fila
    print('Digite:')
    print('\tF para adicionar um cliente ao fim da fila')
    print('\tA para realizar o atendimento')
    print('\tS para sair')
    operacao = raw_input('Operação que deseja realizar: ')
    if operacao == "A":
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print('Cliente %d atendido' %atendido)
        else:
            print('Fila vazia! Não há clientes para atender.')
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print('Operação inválida. Digite apenas F, A ou S.')
