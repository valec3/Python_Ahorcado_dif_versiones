def dibujar_regleta(numerador,denominad=1):
    barra=27
    esp=barra/denominad
    if denominad == 1:
        print("┏" + "━"*27 + "━" + "━"*27 + "┓")
        print("┃" + " "*27 + " " + " "*27 + "┃")
        print("┃" + " "*27 + "1" + " "*27 + "┃")
        print("┃" + " "*27 + " " + " "*27 + "┃")
        print("┗" + "━"*27 + "━" + "━"*27 + "┛")
    elif denominad<=12 and denominad >=10:
        # Imprimir la primera línea del cuadrado
        print("┏" + "━━━" + "┓")

        # Imprimir el numerador
        print("┃" + f" {numerador} " + "┃")

        # Imprimir las líneas intermedias del cuadrado
        print("┃" + "━━━" + "┃")
        
        # Imprimir el denominador
        print("┃" + f"{denominad} " + "┃")
        
        # Imprimir la última línea del cuadrado
        print("┗" + "━━━" + "┛")
    else:
        
        # Imprimir la primera línea del cuadrado
        print("┏" + "━" + "━" + "━" + "┓")

        # Imprimir el numerador
        print("┃" + f" {numerador} " + "┃")

        # Imprimir las líneas intermedias del cuadrado
        print("┃" + "━" + "━" + "━" + "┃")
        
        # Imprimir el denominador
        print("┃" + f" {denominad} " + "┃")
        
        # Imprimir la última línea del cuadrado
        print("┗" + "━" + "━" + "━" + "┛")
    
dibujar_regleta(1,9)
dibujar_regleta(1)
dibujar_regleta(1,12)





