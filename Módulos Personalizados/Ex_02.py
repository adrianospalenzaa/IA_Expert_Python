import Utilitario_02 as ut  # Importa o módulo Utilitario_02.py
import time as tm  # Importa o módulo time.py


nome = ut.mensagem('Digite seu nome: ')
tm.sleep(2)
print(ut.mensagem(f'{nome}, Seu nome e lindo: '))

print(ut.leiaFloat('Digite um número: '))
