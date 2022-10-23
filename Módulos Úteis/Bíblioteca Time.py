import time as tm

print(tm.time())  # Retorna o tempo em segundos desde 1 de janeiro de 1970


antes = tm.time()
lista = []
for i in range(10000):  # Gera uma lista com 10.000 números
    lista.append(i)  # Adiciona um item na lista
depois = tm.time()  # Tempo final

intervalo = depois - antes  # Calcula o tempo de execução
print(f'Tempo: {intervalo} segundos')  # Imprime o tempo de execução

print('finalizado...')
tm.sleep(2)  # Aguarda 2 segundos
print('...')
tm.sleep(2)  # Aguarda 2 segundos
print('Até a próxima!')
