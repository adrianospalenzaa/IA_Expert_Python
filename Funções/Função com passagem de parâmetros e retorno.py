def soma(a, b):  # Função com parâmetro
    return a + b  # Função com retorno


print(soma(2, 3))  # Chamada da função com parâmetro 2 e 3
r = soma(4, 5)
print(r)


def calcula_energia_potencial_gravitacional(m, h, g=9.8):
    # documetação da função
    """
    '''
  Calcula a energia potencial gravitacional
  Argumentos:
  m: massa, entrada como uma variável float
  h: altura, entrada como uma variável float

  Argumento opcional:
  g: aceleração gravitacional, com valor default de 10
  '''
    :param m:
    :param h:
    :param g:
    :return:
    """
    e = g * m * h
    return e  # Função com retorno


print(calcula_energia_potencial_gravitacional(30, 12))  # Chamada da função com parâmetro 2 e 3 g ja definido
print(calcula_energia_potencial_gravitacional(30, 12, 10))  # Chamada da função com parâmetro 2 e 3 g substituido

help(calcula_energia_potencial_gravitacional)  # Help da função