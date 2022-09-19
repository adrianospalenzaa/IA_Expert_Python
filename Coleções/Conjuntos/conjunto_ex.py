biomoleculas = ('DNA', 'RNA', 'Proteínas', 'Lipídeos', 'Carboidratos',
                'RNA', 'Proteínas', 'Lipídeos', 'Carboidratos')  # Tupla
print(biomoleculas)  # Exibe a tupla

print(set(biomoleculas))  # Exibe a tupla sem repetição

conj_1 = {1, 2, 3, 4, 5}  # Cria um conjunto
conj_2 = {3, 4, 5, 6, 7, 8, 9, 10}  # Cria um conjunto
conj_3 = conj_1.union(conj_2)  # Cria um conjunto com a união dos conjuntos 1 e 2
print(conj_3)
conj_4 = conj_1.intersection(conj_2)  # Cria um conjunto com a intersecção dos conjuntos 1 e 2
print(conj_4)
conj_5 = conj_1.difference(conj_2)  # Cria um conjunto com a diferença dos conjuntos 1 e 2
print(conj_5)

