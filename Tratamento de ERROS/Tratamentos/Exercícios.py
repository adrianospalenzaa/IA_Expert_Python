"""
Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas
primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista).
Faça a divisão dos dois valores e trate as seguintes exceções:
– ValueError: se o usuário digitar um caracter
– ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
– IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
– KeyboardInterrupt: caso o usuário interrompa a execução
Mostre uma mensagem personalizada na ocorrência de cada um desses erros
"""

lista = []

for i in range(0, 2):
    valor = float(input(f'Digite o {i + 1}° valor:\n'))
    lista.append(valor)
resul = (lista[0] / lista[1])
print(f'Divisão dos valores é {resul}')
