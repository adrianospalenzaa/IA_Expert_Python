coleta_pessoa = {'nome': 'João', 'idade': 25, 'sexo': 'M', 'peso': 75.8, 'altura': 1.80}
print(coleta_pessoa)
print(coleta_pessoa['nome'])
print(coleta_pessoa['idade'])
print(coleta_pessoa['sexo'])
print(coleta_pessoa['peso'])
print(coleta_pessoa['altura'])

coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}  # Cria um dicionário
print(coleta['Aedes aegypt'])  # Exibe o valor do indice

coleta['Aedes aegypt'] = 33  # Altera o valor do indice
print(coleta['Aedes aegypt'])

coleta['Aedes aegypt'] += 6  # Altera o valor do indice somando mais 6
print(coleta['Aedes aegypt'])

coleta['Aedes aegypt'] -= 6  # Altera o valor do indice subtraindo 6
print(coleta['Aedes aegypt'])

coleta['Aedes aegypt'] *= 6  # Altera o valor do indice multiplicando por 6
print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11  # Adiciona um novo indice
print(coleta)

#del coleta['Rhodnius montenegrensis']  # Remove um indice
#print(coleta)

#coleta.clear()  # Remove todos os indices
#print(coleta)

#del coleta  # Remove o dicionário
#print(coleta)

print(coleta.items())  # Exibe todos os indices e valores

print(coleta.keys())  # Exibe todos os indices do dicionário

print(coleta.values())  # Exibe todos os valores do dicionário

coleta_2 = {'Dengue': 32, 'Sarampo': 22, 'gripe': 14}  # Cria um dicionário
print(coleta_2)

coleta.update(coleta_2)  # Adiciona os indices e valores de um dicionário a outro
print(coleta)

for especie, num_especie in coleta.items():  # Exibe todos os indices e valores
    print(f'{especie}: {num_especie}')
