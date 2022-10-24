while True:
    try:
        p = int(input('Digite um número inteiro: '))
    except ValueError:  # Tratamento de erro para valores inválidos
        print('Valor inválido')
    except KeyboardInterrupt:  # Tratamento de erro para o comando CTRL+C
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'Valor digitado é {p}')
        break
