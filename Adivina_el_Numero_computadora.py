import random


def adivina_el_numero_computadora (x):

    print('=======================================')
    print(' ¡Bienvenido(a) al Juego sapo embarao! ')
    print('=======================================')
    print(f'Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...')

    limite_inferior = 1
    limite_superior = x

    respuesta = ''
    while respuesta != 'c':
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #También podría ser limite superior

        respuesta = input(f'Mi prediccion es {prediccion}. Si es alta, ingresa (a). Si es baja, ingresa (b). Si es correcta, ingresa (c): ').lower()

        if respuesta == 'a':
            limite_superior = prediccion - 1
        elif respuesta == 'b':
            limite_inferior = prediccion + 1

    print(f'La computadora adivino correctamente: {prediccion}')


adivina_el_numero_computadora(10)
