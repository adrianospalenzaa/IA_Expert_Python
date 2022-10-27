with open('frase1.txt', 'r') as tex:  # Abre o arquivo
    for linha in tex:  # Lê o arquivo
        print(linha)  # Imprime o arquivo

with open('frase1.txt') as tex:  # Abre o arquivo
    r = tex.readlines()  # Lê cada linha do arquivo e armazena na variável r
    print(r)

with open('texo2.txt', 'w') as texto:  # Cria o arquivo se não existir
    texto.write('Ola a todos \nBom estudos')  # Escreve no arquivo
    print('Arquivo criado com sucesso')

with open('texo2.txt', 'r') as tex:  # Abre o arquivo
    for linha in tex:  # Lê o arquivo
        print(linha)
