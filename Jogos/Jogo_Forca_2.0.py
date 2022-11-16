import numpy as np
import os

matriz_alfabeto = np.array([['A', 'B', 'C', 'D', 'E'],  # matriz do alfabeto para o usuário
                            ['F', 'G', 'H', 'I', 'J'],
                            ['K', 'L', 'M', 'N', 'O'],
                            ['P', 'Q', 'R', 'S', 'T'],
                            ['U', 'V', 'W', 'X', 'Y'],
                            ['Z', ' ', ' ', ' ', ' ']])


def forca():  # função do jogo da forca
    from random import randint
    p = [['amarelo', 'amiga', 'amor', 'ave', 'aviao', 'avo', 'balao', 'bebe', 'bolo', 'branco', 'cama', 'caneca',
          'celular', 'clube',
          'copo', 'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia', 'girafa', 'janela',
          'limonada', 'mae',
          'meia', 'noite', 'oculos', 'onibus', 'ovo', 'pai', 'pao', 'parque', 'passarinho', 'peixe', 'pijama', 'rato',
          'umbigo'],
         ['afobado', 'amendoim', 'banheiro', 'caatinga', 'cachorro', 'campeonato', 'capricornio',
          'catapora', 'corrupcao', 'crepusculo', 'empenhado', 'esparadrapo', 'forca', 'galaxia', 'historia', 'magenta',
          'manjericao', 'menta',
          'moeda', 'oracao', 'pacoca', 'palavra', 'pedreiro', 'pneumonia', 'pulmao', 'rotatoria', 'serenata',
          'transeunte', 'trilogia', 'xicara'],
         ['acender', 'afilhado', 'ardiloso', 'aspero', 'assombracao', 'asterisco', 'basquete', 'caminho', 'champanhe',
          'chiclete', 'chuveiro',
          'coelho', 'contexto', 'convivencia', 'coracao', 'desalmado', 'eloquente', 'esfirra', 'esquerdo', 'excecao',
          'fugaz', 'gororoba',
          'heterossexual', 'horrorizado', 'impacto', 'independencia', 'modernidade', 'oftalmologista',
          'otorrinolaringologista', 'paralelepipedo',
          'pororoca', 'prognosticio', 'quarentena', 'quimera', 'refeicao', 'reportagem', 'sino', 'taciturno', 'tenue',
          'visceral']]  # lista de palavras por dificuldade (facil, medio, dificil)
    print('-=' * 20)  # printa uma linha
    print('JOGO DA FORCA')
    print('-=' * 20)
    while True:  # loop para escolher dificuldade
        print('[1] Fácil \n[2] Médio\n[3] Difícil')
        modo = int(input('Escolha o modo de jogo: '))
        if modo == 1 or modo == 2 or modo == 3:  # Verifica se o modo escolhido é válido
            break  # sai do loop

    pal = p[modo - 1][randint(0, len(p[modo - 1]))]  # escolhe uma palavra aleatória do modo escolhido
    usadas = ''  # letras usadas
    q_caract = '_' * len(pal)  # palpite
    if modo == 1:  # define o número de tentativas de acordo com o modo escolhido
        vidas = 7
    elif modo == 2:
        vidas = 5
    elif modo == 3:
        vidas = 3
    while True:  # loop do jogo em si (enquanto o jogador não acertar ou perder)
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa o terminal depois de cada escolha
        print(f'Vidas : {vidas}')  # mostra o número de tentativas restantes
        print(f'Letras usadas: {usadas}.')  # mostra as letras usadas
        print(f'Palavra secreta-->  {q_caract}')  # mostra a palavra com a quantidade de caracteres

        cont_linha = 0
        print('-=' * 6)
        print('0-1-2-3-4 -=')
        print('-=' * 6)
        for linha in range(0, 6):
            for coluna in range(0, 5):
                print(f'{matriz_alfabeto[linha, coluna]}', end=' ')  # mostra a matriz do alfabeto para o usuário
            print(f'-= {cont_linha}')
            cont_linha += 1
            print()
        print('-=' * 6)

        linha = int(input('Digite a posição da linha: '))
        coluna = int(input('Digite a posição da coluna: '))
        print(f'Letra: {matriz_alfabeto[linha, coluna]}')
        l_matris = matriz_alfabeto[linha, coluna]  # letra escolhida pelo usuário

        t = l_matris.lower()  # transforma a letra em minúscula
        x = 0  # contador
        for i in range(len(pal)):  # verifica se a letra digitada está na palavra
            if t == pal[i]:  # se estiver, substitui o '_' pelo caractere
                t1 = q_caract[0:i]
                t2 = q_caract[i + 1:len(q_caract)]
                q_caract = t1 + t + t2  # substitui o '_' pelo caractere
            else:
                x += 1
        usadas += ' ' + t  # adiciona a letra usada na string de letras usadas
        if x == len(pal):  # se a letra não estiver na palavra, perde uma tentativa
            vidas -= 1  # perde uma tentativa

        if vidas == 0 or q_caract == pal:  # se o jogador perder todas as tentativas ou acertar a palavra, o jogo acaba
            print('-=' * 20)
            print(f'A palavra era {pal}!')
            break
    if vidas == 0:
        print('\033[033mGame Over!\033[m Tente novamente.')  # mensagem de derrota
    else:
        print('\033[035mParabens você venceu!!\033[m Tente um nível mais dificil!')  # mensagem de vitória


while True:  # loop para jogar novamente
    forca()  # chama a função do jogo
    n = ' '
    while n not in 'nNsS':  # verifica se o usuário quer jogar novamente
        n = input('\nJogar novamente[S]/[N]? ').upper()[0]  # pergunta se o usuário quer jogar novamente
    if n == 'N':
        break  # se não, o jogo acaba
os.system('cls' if os.name == 'nt' else 'clear')  # limpa o terminal antes de começar
