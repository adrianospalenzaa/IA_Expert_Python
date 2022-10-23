def soma(a, b, c):  # Função soma
    somatorio = a+b+c
    return somatorio


def mult(a, b, c):  # Função multiplicação
    produto = a*b*c
    return produto


def ispalindromo(string):   # Função que verifica se uma string é palíndromo
    if string == string[::-1]:
        return True
    else:
        return False


def divisao(a, b):  # Função divisão
    return a/b
