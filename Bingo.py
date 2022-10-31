"""
Faça um programa para gerar automaticamente números entre 0 e 99 de cinco cartelas de bingo.
Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter
números repetidos dentro das cartelas. O programa deve exibir na tela as cinco cartelas geradas.
Após, gere números aleatórios até que uma das cartelas seja a ganhadora.
"""

import random  # Importa a biblioteca random

cartelas = []
for i in range(5):
    cartela = []
    for j in range(5):
        linha = []
        for k in range(5):
            linha.append(random.randint(0, 99))  # Gera um número aleatório entre 0 e 99
        cartela.append(linha)
    cartelas.append(cartela)

for i in range(5):
    print('Cartela', i + 1)
    for j in range(5):
        print(cartelas[i][j])
    print()

numeros = []
while True:  # Loop infinito  # Enquanto verdadeiro
    numero = random.randint(0, 99)  # Gera um número aleatório entre 0 e 99
    if numero not in numeros:
        numeros.append(numero)
        for i in range(5):
            for j in range(5):
                if numero in cartelas[i][j]:
                    cartelas[i][j].remove(numero)  # Remove o número da lista
                    if len(cartelas[i][j]) == 0:
                        print('Cartela', i + 1, 'ganhou!')
                        exit()
        print(numero)
