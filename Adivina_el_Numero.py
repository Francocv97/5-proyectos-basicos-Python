import random


def adivina_el_numero (x):

    print('=======================================')
    print(' ¡Bienvenido(a) al Juego sapo embarao! ')
    print('=======================================')
    print('Tu meta es adivinar el número generado por la computadora')

    numero_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x

    predicción = 0

    while predicción != numero_aleatorio:
        #El usuario ingresa un número
        predicción = int(input(f'Adivina un número entre 1 y {x}: ')) # f-string

        if predicción < numero_aleatorio:
            print('Intenta otra vez, el número es muy pequeño')

        elif predicción > numero_aleatorio:
            print('Intenta otra vez, el número es muy grande')

    print(f'¡Felicitaciones lonji culeco! Adivinaste el número {numero_aleatorio} correctamente')


adivina_el_numero(10)

    

