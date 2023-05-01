import random
import time
import os

opciones = ["piedra", "papel", "tijeras"]
puntajes = {"usuario": 0, "bot": 0}

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_pensando():
    print("El bot está pensando...", end="", flush=True)
    time.sleep(0.9)
    print("\r                   \r", end="", flush=True)

def obtener_mov_usuario():
    while True:
        mov = input("Elige piedra, papel o tijeras: ").lower()
        if mov in opciones:
            return mov
        print("Entrada inválida, por favor inténtalo de nuevo.")

def obtener_mov_bot():
    mostrar_pensando()
    return random.choice(opciones)

def determinar_ganador(mov_usuario, mov_bot):
    if mov_usuario == mov_bot:
        print("Empate.")
        return "empate"
    elif (mov_usuario == "piedra" and mov_bot == "tijeras") or \
         (mov_usuario == "tijeras" and mov_bot == "papel") or \
         (mov_usuario == "papel" and mov_bot == "piedra"):
        print("Ganaste!")
        return "usuario"
    else:
        print("Perdiste :(")
        return "bot"

def mostrar_puntajes():
    print(f"{puntajes['usuario']} - {puntajes['bot']}")

def resetear_puntajes():
    puntajes["usuario"] = 0
    puntajes["bot"] = 0

def jugar_nueva_partida():
    global puntajes
    puntajes = {"usuario": 0, "bot": 0}
    while True:
        clear_console()
        mostrar_puntajes()
        mov_usuario = obtener_mov_usuario()
        mov_bot = obtener_mov_bot()
        ganador = determinar_ganador(mov_usuario, mov_bot)
        if ganador != "empate":
            puntajes[ganador] += 1
        if puntajes["usuario"] == 3 or puntajes["bot"] == 3:
            print(f"El ganador es {'usuario' if puntajes['usuario'] == 3 else 'bot'}")
            break

def main():
    while True:
        clear_console()
        print("Bienvenido al juego de Piedra, Papel o Tijeras")
        jugar_nueva_partida()
        reiniciar_juego = input("¿Quieres jugar de nuevo? (s/n)").lower()
        if reiniciar_juego != "s":
            break
    print("Gracias por jugar, ¡hasta la próxima!")

if __name__ == "__main__":
    main()
