from time import sleep

print('\033[32mx\033[m'*40)
print('|{:^38}|'.format('Criação de personagem'))
print('\033[32mx\033[m'*40)


print('Vamos escolher o gênero do seu personagem:')
print('Escolha:')
print('[F] Feminino')
print('[M] Masculino')
gender = ''
while gender != 'F' and gender != 'M':
    gender = input('Insira o gênero desejado: ').upper()

    if gender == 'F':
        print('O gênero escolhido foi \033[31mFEMININO\033[m.')
    elif gender == 'M':
        print('O gênero escolhido foi \033[34mMASCULINO\033[m.')
        gender.join(gender)
    else:
        print('Opção Inválida tente novamente!')

sleep(1)

print('Agora vamos escolher a cor dos olhos:')
print('Escolha:')
print('''[1] Azul
[2] Verde
[3] Preto
[4] Castanho
[5] Vermelho''')
eye = 0
while not eye == 1 and not eye == 2 and not eye == 3 and not eye == 4 and not eye == 5:
    eye = int(input('Insira a cor dos olhos: '))
    if eye == 1:
        print('A cor \033[34mAZUL\033[m foi escolhida com sucesso!')
    elif eye == 2:
        print('A cor \033[33mVERDE\033[m foi escolhida com sucesso!')
    elif eye == 3:
        print('A cor \033[30mPRETO\033[m foi escolhida com sucesso!')
    elif eye == 4:
        print('A cor CASTANHO foi escolhida com sucesso!')
    elif eye == 5:
        print('A cor \033[31mAZUL\033[m foi escolhida com sucesso!')
    else:
        print('Opção Inválida tente novamente!')
sleep(1)

print('Agora vamos escolher a cor do cabelo:')
print('Escolha:')
print('''[1] Castanho
[2] Preto
[3] Loiro
[4] Vermelho 
[5] Branco''')
hair = 0
while not hair == 1 and not hair == 2 and not hair == 3 and not hair == 4 and not hair == 5:
    hair = int(input('Insira a cor do cabelo: '))
    if hair == 1:
        print('A cor CASTANHO foi escolhida com sucesso!')
    elif hair == 2:
        print('A cor PRETO foi escolhida com sucesso!')
    elif hair == 3:
        print('A cor LOIRO foi escolhida com sucesso!')
    elif hair == 4:
        print('A cor VERMELHO foi escolhida com sucesso!')
    elif hair == 5:
        print('A cor BRANCO foi escolhida com sucesso!')
    else:
        print('Opção Inválida tente novamente!')
sleep(1)

print('Escolha a sua classe:')
print('''[1] Guerreiro(a)
[2] Arqueiro(a)
[3] Mago(a)
[4] Assassino(a)
[5] Clérigo(a)''')
classe = 0
while not classe == 1 and not classe == 2 and not classe == 3 and not classe == 4 and not classe == 5:
    classe = int(input('Insira classe desejada: '))
    if classe == 1:
        print('A classe GUERREIRO(A) foi escolhida com sucesso!')
    elif classe == 2:
        print('A classe ARQUEIRO(A) foi escolhida com sucesso!')
    elif classe == 3:
        print('A classe MAGO(A) foi escolhida com sucesso!')
    elif classe == 4:
        print('A classe ASSASSINO(A) foi escolhida com sucesso!')
    elif classe == 5:
        print('A classe CLÉRIGO(A) foi escolhida com sucesso!')
    else:
        print('Opção Inválida tente novamente!')
sleep(1)
print('\033[31mVocê criou seu personagem com sucesso!\033[m')
print('\033[31mBom jogo!\033[m')
