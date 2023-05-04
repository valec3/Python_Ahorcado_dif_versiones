n = 7

for i in range(1, n+1):
    # Imprimir espacios en blanco
    print(" "*(n-i), end="")
    
    # Imprimir números en orden ascendente
    for j in range(1, i+1):
        print(j, end="")
    
    # Imprimir números en orden descendente
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()