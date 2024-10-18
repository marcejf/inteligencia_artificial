# Número de filas para la mitad superior del rombo
filas = 5

# Parte superior del rombo
for i in range(1, filas + 1):
    # Imprimir espacios
    print(' ' * (filas - i), end='')
    # Imprimir asteriscos
    print('* ' * i)

# Parte inferior del rombo
for i in range(filas - 1, 0, -1):
    # Imprimir espacios
    print(' ' * (filas - i), end='')
    # Imprimir asteriscos
    print('* ' * i)
