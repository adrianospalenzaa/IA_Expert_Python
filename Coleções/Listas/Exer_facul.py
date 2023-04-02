import numpy as np
cont = 0
nome = np.array(['t','i','a','g','o'])
for i in range(5):
    print(nome[0:5])
    print(id(nome[0:5]))
    nome = np.delete(nome, cont)
    cont += 0








