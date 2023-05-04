import time

span_texto = "-"*50
cadena = list(span_texto)
for i in range(50):
    cadena[i]="#"
    cadena_imp = "".join(cadena)
    print(f"{cadena_imp}{i*2}%",end="\r")
    time.sleep(.1)
        