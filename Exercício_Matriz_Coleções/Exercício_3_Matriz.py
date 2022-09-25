"""
# Exercício 3: Matriz

Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
matriz
[3, 4, 1]
[3, 1, 5]

"""
import numpy as np

matriz = np.array([[3, 4, 1],  # Cria uma matriz
                   [3, 1, 5]])
print(matriz.shape)  # Retorna a dimensão da matriz

soma = 0
for linha in range(matriz.shape[0]):  # Percorre as linhas da matriz
    for colun in range(matriz.shape[1]):  # Percorre a matriz coluna por coluna
        #print(matriz[linha][colun]) #percorre a matriz e imprime os elementos
        soma = soma + matriz[linha][colun]  # Soma os elementos da matriz
print(soma)  # Imprime a soma dos elementos da matriz
