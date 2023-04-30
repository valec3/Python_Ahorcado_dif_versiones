import random

palabras = ["Arbol","Licuadora","Mesa","Celeste","Persona","Mirador","Comunicar","Reciclar"]
vidas = 6
letras_adivinadas=set()
gameover=False


class ExcessiveAttempts(Exception):
    """Exception raised for excesive intents

    Attributes:
        message
    """
    def __init__(self, mensaje="Demasiados intentos invalidos :)"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def elegir_palabra(words):
    palabra = random.choice(words).upper()
    return palabra

def pedir_letra():
    letra=""
    tolerancia=5
    while len(letra)!=1 or letra.isalpha()==False:
        letra = input("Ingresa una letra (a-b/A-B): ").upper()
        tolerancia-=1
        if tolerancia == 0:
            raise ExcessiveAttempts()
    return letra

def mostrar_tablero(palabra):
    texto_mostrar=[]
    for l in palabra:
        if l in letras_adivinadas:
            texto_mostrar.append(l)
        else:
            texto_mostrar.append("_")
    print(f"Vidas: {vidas}\n","--"*len(palabra))
    print(" ".join(texto_mostrar)) 
    print("--"*len(palabra))

def buscar_letra(letra,palabra):
    global vidas
    if letra in letras_adivinadas:
        print("Ya has ingresado esa letra. Intenta con otra.")
        vidas-=1
    elif letra in palabra:
        letras_adivinadas.add(letra)
    else:
        print("La letra no está en la palabra.")
        vidas -= 1

def juego(gameover):
    palabra_elegida=elegir_palabra(palabras)
    while not gameover:
        letra_ingresada=pedir_letra()
        buscar_letra(letra_ingresada,palabra_elegida)
        mostrar_tablero(palabra_elegida)
        if vidas==0:
            print("="*10,f"\nPERDISTE \nLa palabra era: {palabra_elegida} \n","="*10)
            break
        elif letras_adivinadas==set(palabra_elegida):
            print("="*10,"\nGANASTE\n","="*10)
            break


juego(gameover)

