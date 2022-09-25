"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro.
Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
 Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
 Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
 com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
 tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
– Função para ler os valores (não recebe parâmetro e retorna os dois valores)
– Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
– Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
– Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
"""

"""fornecer o tempo gasto na viagem e a velocidade média durante ela."""


def info_viagem():
    tempo = float(input('Tempo gasto: '))
    veloc = float(input('Velocidade media: '))
    return tempo, veloc


def calc_distancia(tempo, veloc):
    distancia = tempo * veloc
    return distancia


def quant_litros(distancia):
    litros = distancia / 12
    return litros


def main():
    tempo, veloc = info_viagem()
    distancia = calc_distancia(tempo, veloc)
    litros = quant_litros(distancia)
    print(f'velocidade media na viagem foi: {veloc}')
    print(f'Tempo gasto na viagem foi: {tempo}')
    print(f'Distancia gasto na viagem foi: {distancia}')
    print(f'Litros gasto na viagem foi: {litros}')


if __name__ == '__main__':
    main()
