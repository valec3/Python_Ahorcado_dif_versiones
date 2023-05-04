numeros = [47,48,57,69,58,12,45,56,35,91,28,17,39,97]

def metodo_insercion(lista):
    aux=0
    for i,_ in enumerate(lista):
        aux=lista[i]
        while i > 0 and lista[i-1] > aux:
            lista[i] = lista[i-1]
            i-=1
        lista[i]=aux
    return lista

print(metodo_insercion(numeros))