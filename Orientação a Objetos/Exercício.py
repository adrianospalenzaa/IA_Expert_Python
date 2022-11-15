"""
  1-Crie uma classe chamada aluno com os seguintes atributos:
– Nome
– Nota 1
– Nota 2
– Crie um construtor para a classe (__init__)

  2-Crie as seguintes funções (métodos):
– Calcula média, retornando a média aritmética entre as notas
– Mostra dados, que somente imprime o valor de todos os atributos
– Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior
  ou igual a 6.0, o aluno está aprovado)

  3-Crie dois objetos (aluno1 e aluno2) e teste as funções
"""


class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostra_dados(self):
        print('Nome:', self.nome)
        print('nota 1:', self.nota1)
        print('Nota 2:', self.nota2)
        print('Média:', self.media)

    def resultado(self):
        if self.media >= 6:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')


aluno1 = aluno('adriano', 1.5, 10.0)
media = aluno1.calcula_media()
aluno1.mostra_dados()
aluno1.resultado()

aluno2 = aluno('joao', 10.0, 10.0)
media = aluno2.calcula_media()
aluno2.mostra_dados()
aluno2.resultado()
