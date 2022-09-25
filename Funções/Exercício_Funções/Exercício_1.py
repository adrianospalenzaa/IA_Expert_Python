"""
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C
é a temperatura em graus Celsius
– Função para ler e retorna o valor da temperatura (não recebe parâmetro)
– Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
– Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão
"""


def ler_temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura


def conver_temp(temperatura):
    f = (9 * temperatura + 160) / 5
    return f


def resultado(f):
    print(f'A temperatura em graus Fahrenheit é: {f}')


def main():
    temperatura = ler_temperatura()
    f = conver_temp(temperatura)
    resultado(f)


if __name__ == '__main__':
    main()
