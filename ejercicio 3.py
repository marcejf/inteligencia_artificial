def crear_matriz_escalonada():
    # Crear una matriz de 6x6 con la forma escalonada deseada
    matriz = [
        [1, 1, 1, 1, 1, 1],  # Fila 1
        [0, 1, 1, 1, 1, 1],  # Fila 2
        [0, 0, 1, 1, 1, 1],  # Fila 3
        [0, 0, 0, 1, 1, 1],  # Fila 4
        [0, 0, 0, 0, 1, 1],  # Fila 5
        [0, 0, 0, 0, 0, 1]   # Fila 6
    ]
    
    # Imprimir la matriz fila por fila
    for fila in matriz:
        print(fila)

# Llamada a la función
crear_matriz_escalonada()
