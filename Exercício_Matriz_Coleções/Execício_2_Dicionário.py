"""
Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos,
fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova
estrutura de repetição para somar todas as notas e retornar a média
"""
dic_aluno = {}  # Cria um dicionário vazio
for cont in range(1, 4):
    nome = input(f'Informe o nome do {cont}° aluno: ')
    nota = float(input(f'Informe a nota do {cont}° aluno: '))
    dic_aluno[nome] = nota  # Adiciona o nome e a nota no dicionário OBS: nome é a chave e nota é o valor
print(dic_aluno)

print(dic_aluno['adriano'])  # Imprime a nota do aluno Adriano
print(dic_aluno.values())  # Imprime as notas dos alunos
print(dic_aluno.keys())  # Imprime os nomes dos alunos
print(dic_aluno.items())  # Imprime os nomes e as notas dos alunos


soma = 0
for cont in dic_aluno.values():  # Percorre o dicionário
    soma += cont
print(f'A média das notas dos alunos é: {soma / len(dic_aluno)}')
# Soma as notas dos alunos e divide pelo número de alunos
