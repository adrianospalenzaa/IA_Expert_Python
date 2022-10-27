"""
Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie
uma estrutura de repetição para percorrer cada elemento do dicionário para gravar
cada aluno em um novo arquivo de texto
– Cada aluno deve ocupar uma linha do novo arquivo de texto
– O formato deve ser: nome,nota (Pedro,8.0)
– Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos
alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
"""

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}  # Cria um dicionário com os alunos e suas notas

with open('alunos.txt', 'w') as arquivos:  # Cria o arquivo alunos.txt  # OBS: 'w' sobrescreve o arquivo
    for aluno, nota in alunos.items():  # Percorre o dicionário alunos  # OBS: aluno é a chave e nota é o valor
        arquivos.write(f'{aluno},{nota} \n')  # Escreve no arquivo alunos.txt

with open('alunos.txt', 'r') as arquivos:  # Abre o arquivo alunos.txt
    for linha in arquivos:  # Percorre o arquivo alunos.txt
        print(linha)
