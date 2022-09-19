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
    