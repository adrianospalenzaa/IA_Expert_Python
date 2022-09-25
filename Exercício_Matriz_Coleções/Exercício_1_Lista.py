"""
1-Lista: Crie uma estrutura de repetição para fazer a leitura de 5
números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra
estrutura de repetição para somar todos os valores digitados
"""
import numpy as np
lista = []  # Cria uma lista vazia
for cont in range(0, 4):
    num = int(input(f'Digite o {cont + 1}° número: '))  # Lê o número
    lista.append(num)  # Adiciona o número na lista

#soma = 0
#for cont in range(len(lista)): # Percorre a lista #len = comprimento da lista
    #soma += lista[cont]
#print(f'A soma dos números digitados é: {soma}')


print(f'A soma dos números digitados é: {np.array(lista).sum()}')  # Soma os números da lista
