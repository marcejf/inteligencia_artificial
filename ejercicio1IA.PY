def imprimir_impares_inverso(inicio, fin):
    # Recorremos el rango de fin a inicio, y verificamos si el número es impar
    for num in range(fin, inicio - 1, -1):
        if num % 2 != 0:
            print(num)

# Ejemplo de uso
imprimir_impares_inverso(1, 20)
