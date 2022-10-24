while True:  # Loop infinito
    try:
        n = int(input('Digite um número inteiro: '))  # Recebe um valor inteiro
    except:  # Tratamento de erro para qualquer tipo de erro
        print('Valor inválido')  # Mensagem de erro
    else:
        print(f'Valor digitado é {n}')
        break  # Interrompe o loop infinito
