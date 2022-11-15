import numpy as np  # Importa o módulo numpy, (np é um apelido para numpy )

matriz = np.array([[1, 2, 3], [4, 5, 7]])  # Cria uma matriz

print(matriz)  # Exibe a matriz

print(matriz.shape)  # Exibe a forma da matriz

print(matriz[1])  # Exibe a primeira linha da matriz

print(matriz[0][2])  # Exibe o terceiro elemento da primeira linha da matriz

for linha in range(matriz.shape[0]):
    print(matriz[linha])  # Exibe todas as linhas da matriz
    for coluna in range(matriz.shape[1]):
        print(matriz[linha][coluna])  # Exibe todos os elementos da matriz

for linha in matriz:  # Exibe todos os elementos da matriz
    print(linha)

matriz_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [99, 88, 55, 63]])
print(matriz_2)

"""criar matris 5 linha e 5 coluna automaticamente"""
matriz_3 = np.random.randint(0, 100, (5, 5))
# Cria uma matriz 5x5 com números aleatórios entre 0 e 99
print(matriz_3)
print(matriz_3.shape)
print(matriz_3[0][2]) # Exibe o terceiro elemento da primeira linha da matriz

'criar matriz vazia tamanho indeterminado'

matriz_velha = np.empty((3, 3), int)  # Cria uma matriz vazia
print(matriz_velha)

for linha in range(matriz_velha.shape[0]):
    for coluna in range(matriz_velha.shape[1]):
        matriz_velha[linha][coluna] = int(input('Digite um número: '))

print(matriz_velha)


#matriz_jogo_velha = np.array([['0', '0', '1'], ['1', '0', '1'], ['0', '1', '0']])
#print(matriz_jogo_velha)

#matriz_jogo_velha[0][0] = '1'  # Altera o elemento da primeira linha e primeira coluna
#print(matriz_jogo_velha)

