import random

attemps=0
min_number=1
max_number=20

usuario_name=input("Hola, cual es tu nombre: ")
number_choice=random.randint(min_number,max_number)
print(f"Hola {usuario_name} estoy pensando en un numero entre {min_number} y {max_number}")

while attemps < 7:
    number=int(input("Ingresa un numero: "))
    attemps+=1
    
    if number < number_choice:
        print("El numero ingresado es menor a mi numero")
    elif number > number_choice:
        print("El numero ingresado es mayor a mi numero")
    else:
        break

if number_choice == number:
    print(f"Has adivinado mi numero en {attemps} intentos")
else:
    print("Has perdido, el numero que estaba pensando era {number_choice}")




