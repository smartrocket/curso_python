#-*- encoding: utf-8 -*-
pontos = 0
questao = 1
while questao <= 3:
    resposta = raw_input('Resposta da questão %d: ' %questao)
    if questao == 1 and resposta == 'c':
        pontos = pontos + 1
    if questao == 2 and resposta == 'b':
        pontos = pontos + 1
    if  questao == 3 and resposta == 'd':
        pontos = pontos + 1
    questao += 1
print('O candidato fez %d ponto(s)' %pontos)
