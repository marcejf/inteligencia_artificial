# Número de filas
filas = 5

# Generar el triángulo invertido
for i in range(filas, 0, -1):
    # Imprimir espacios
    print(' ' * (filas - i), end='')
    # Imprimir asteriscos
    print('* ' * i)

