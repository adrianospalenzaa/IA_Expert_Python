l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Homen', 'Cachorro', 'Gato']

print(l1 + l2)  # soma e exibe as duas listas

l3 = l2 * 2  # duplica a lista
print(l3)

print(l1[2])
print(l2[0:3])

for elemento in l1:  # Exibe todos os elementos da lista
    print(elemento)

l2.append('Papagaio')  # adiciona um elemento na lista
print(l2)

l2.insert(0, 'Elefante')  # adiciona um elemento na lista em um indice especifico
print(l2)

l2.remove('Elefante')  # remove um elemento da lista
print(l2)

l2.pop(3)  # remove um elemento da lista em um indice especifico
print(l2)

l2.pop()  # remove o ultimo elemento da lista
print(l2)

l2.clear()  # remove todos os elementos da lista
print(l2)

del l2  # remove a lista
