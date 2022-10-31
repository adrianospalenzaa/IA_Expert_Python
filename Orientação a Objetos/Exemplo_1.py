class triangulo:  # Criação da classe
    def __init__(self, lado1, lado2, lado3, base, altura):  # Método construtor
        self.lado1 = lado1  # Atributos
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):  # Método da classe triangulo para calcular a área
        return (self.base * self.altura) / 2

    def tipo(self):  # Método da classe triangulo para verificar o tipo do triângulo
        if self.lado1 > self.lado2 + self.lado3:  # Verifica se o lado1 é maior que a soma dos outros dois lados
            return 'Não é um triângulo'  # Retorna a mensagem
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
            # Verifica se o lado1 é igual a algum outro lado
            return 'Isósceles'  # Retorna a mensagem
        else:
            return 'Outro tipo de triângulo'


t1 = triangulo(5, 1, 3, 4, 3)  # Instância da classe
print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)  # Acesso aos atributos
print(t1.area())  # Acesso ao método
print(t1.tipo())

t2 = triangulo(8, 8, 8, 9, 10)
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)
print(t2.area())
print(t2.tipo())
