numeros = [0, 23, 45, 21, 1, 56, 88, 49, 78, 54, 6, 98, 70]

numeros.sort()

def busqueda_binaria(valor):
    inicio=0
    final=len(numeros)-1
    while inicio <= final:
        mitad=(inicio+final)//2
        if valor == numeros[mitad]:
            return mitad
        elif valor > numeros[mitad]:
            inicio = mitad + 1
        else:
            final = mitad - 1
            
    return None

def busqueda_secuencial(valor):
    for i, elemento in enumerate(numeros):
        if elemento == valor:
            return i
    return -1

def busqueda_interpolacion( valor):
    inicio = 0
    fin = len(numeros) - 1
    while inicio <= fin and valor >= numeros[inicio] and valor <= numeros[fin]:
        posicion = inicio + int(((float(fin - inicio) / (numeros[fin] - numeros[inicio])) * (valor - numeros[inicio])))
        if numeros[posicion] == valor:
            return posicion
        elif numeros[posicion] < valor:
            inicio = posicion + 1
        else:
            fin = posicion - 1
    return -1

def busqueda_hash( valor):
    tabla_hash = {}
    for i, elemento in enumerate(numeros):
        tabla_hash[elemento] = i
    if valor in tabla_hash:
        return tabla_hash[valor]
    else:
        return -1


def buscar(tipo_busqueda,valor):
    print(f"EL numero {valor} se encuentra en { tipo_busqueda(valor) }")

buscar(busqueda_binaria,21)
buscar(busqueda_secuencial,21)
buscar(busqueda_interpolacion,21)
buscar(busqueda_hash,21)