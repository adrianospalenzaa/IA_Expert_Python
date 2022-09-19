"""
Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos,
fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova
estrutura de repetição para somar todas as notas e retornar a média
"""
dic_aluno = {}
for cont in range(1, 4):
    nome = input(f'Informe o nome do {cont}° aluno: ')
    nota = float(input(f'Informe a nota do {cont}° aluno: '))
    dic_aluno[nome] = nota
print(dic_aluno)