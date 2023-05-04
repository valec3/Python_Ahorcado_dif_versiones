def encriptar_basico_re(frase,caracter="x"):
    frase_encriptada=""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                frase_encriptada+=caracter.upper()
            else:
                frase_encriptada+=caracter.lower()
        else:
            frase_encriptada+=letra
    return frase_encriptada

def cifrado_cesar():
    """_summary
    Funcion para cifrar usando el metodo cesar
    """
    pass



frase="Hola mundo, Juan y Ana. Estan BIEN"
print(encriptar_basico_re(frase,"o"))