def cifrado_cesar(mensaje, desplazamiento):
    cifrado = ''
    for letra in mensaje:
        if letra.isalpha():
            codigo = ord(letra) + desplazamiento
            if letra.isupper():
                cifrado += chr((codigo - 65) % 26 + 65)
            else:
                cifrado += chr((codigo - 97) % 26 + 97)
        else:
            cifrado += letra
    return cifrado

print(cifrado_cesar("Este mensaje es secreto aña",7))
