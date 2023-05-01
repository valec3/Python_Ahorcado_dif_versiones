import random
import time
import os

opciones="piedra","papel","tijeras"
os.system("cls")
usuario=input("Ingresa tu nombre: ")
gameover=False
puntaje_usuario = 0
puntaje_bot = 0

def mostrar_pensando():
    print("El bot esta pensando...", end="", flush=True)
    time.sleep(0.9)  
    print("\r                   \r",end="",flush=True)  # Borra el mensaje

print(f"\nBienvenido(a), {usuario}!\n")

while not gameover:
    os.system("cls")
    print("JUGANDO\n","-"*20)
    usuario_mov = input("Elige piedra/papel/tijera: ").lower()
    if usuario_mov not in opciones:
        os.system("cls")
        print("\n|¡ Entrada invalida ! |")
        time.sleep(0.6)
        continue
    bot_mov = random.choice(opciones)
    print(f"Has elegido {usuario_mov}")
    mostrar_pensando()
    print(f"El bot ha elegido {bot_mov}")
    if bot_mov==usuario_mov:
        print("Empate")
    elif (usuario_mov, bot_mov) in (("piedra", "tijeras"), ("tijeras", "papel"), ("papel", "piedra")):
        print("Ganaste!")
        puntaje_usuario+=1
    else:
        print("Perdiste :(")
        puntaje_bot += 1
    repetir=input("¿Quieres volver a jugar? Y/N :").upper()
    gameover=False if repetir=="Y" else True
    
print(f"\nPuntaje final:\n{usuario}: {puntaje_usuario}\nBot: {puntaje_bot}")
print("¡Gracias por jugar!")