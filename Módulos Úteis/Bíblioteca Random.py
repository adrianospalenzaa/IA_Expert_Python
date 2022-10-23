import random

random.random()  # Gera um número aleatório entre 0 e 1
print(random.random())


random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
print(random.randint(1, 10))


random.randrange(0, 10, 2)  # Gera um número aleatório entre 0 e 10 pulando de 2 em 2
print(random.randrange(0, 10))

x = ['k', 'd', 13, '34-j', 'x']
random.choice(x)  # Escolhe um item aleatório da lista
print(random.choice(x))

