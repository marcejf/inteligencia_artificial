def imprimir_impares_inverso(inicio, fin):
    # Lista de números impares en el rango inverso
    impares = [str(num) for num in range(fin, inicio - 1, -1) if num % 2 != 0]
    
    # Imprimir los números separados por comas
    print(", ".join(impares))

# Ejemplo de uso
imprimir_impares_inverso(1, 20)
