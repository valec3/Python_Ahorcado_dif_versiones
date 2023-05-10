import os
def dibujar_regleta(numerador,denominad=1):
    barra=120
    esp=(barra//denominad - 5) // 2 + 1
    # print(esp)
    cuerpo_a="┏" + "━"*(esp-1) + "━━━" + "━"*esp + "┓"
    cuerpo_b="┃" + " "*(esp-1) +f" {numerador} "+" "*esp + "┃"
    cuerpo_c="┃" + "━"*(esp-1) + "━━━" + "━"*esp + "┃"
    cuerpo_d="┃" + " "*(esp-1) +f" {denominad} "+" "*esp + "┃"
    cuerpo_e="┗" + "━"*(esp-1) + "━━━" + "━"*esp + "┛"
    if denominad == 1:
        print("┏" + "━"*57 + "━━━" + "━"*58 + "┓")
        print("┃" + " "*57 + "   " + " "*58 + "┃")
        print("┃" + " "*57 + " 1 " + " "*58 + "┃")
        print("┃" + " "*57 + "   " + " "*58 + "┃")
        print("┗" + "━"*57 + "━━━" + "━"*58 + "┛")
        return
    elif denominad<=12 and denominad >9:
        cuerpo_a="┏" + "━"*(esp) + "━━━"            + "━"*(esp-1) + "┓"
        cuerpo_b="┃" + " "*(esp) + f" {numerador} " + " "*(esp-1) + "┃"
        cuerpo_c="┃" + "━"*(esp) + "━━━"            + "━"*(esp-1) + "┃"
        cuerpo_d="┃" + " "*(esp) + f"{denominad} "  + " "*(esp-1) + "┃"
        cuerpo_e="┗" + "━"*(esp) + "━━━"            + "━"*(esp-1) + "┛"
    elif denominad == 8:
        esp=5
        cuerpo_a="┏" + "━"*(esp) + "━━━"            + "━"*(esp) + "┓"
        cuerpo_b="┃" + " "*(esp) + f" {numerador} " + " "*(esp) + "┃"
        cuerpo_c="┃" + "━"*(esp) + "━━━"            + "━"*(esp) + "┃"
        cuerpo_d="┃" + " "*(esp) + f" {denominad} " + " "*(esp) + "┃"
        cuerpo_e="┗" + "━"*(esp) + "━━━"            + "━"*(esp) + "┛"
    print(cuerpo_a*denominad)
    print(cuerpo_b*denominad)
    print(cuerpo_c*denominad)
    print(cuerpo_d*denominad)
    print(cuerpo_e*denominad)
        
def preguntar():
    print("Regletas: 1 - 1/2 - 1/3 - 1/4 - 1/5 - 1/6 - 1/8 - 1/10 - 1/12")
    regletas={"1":(1,1),"1/2":(1,2),"1/3":(1,3),"1/4":(1,4),"1/5":(1,5),"1/6":(1,6),"1/8":(1,8),"1/10":(1,10),"1/12":(1,12)}
    regleta_1=input("Elija una regleta: ")
    regleta_2=input("Elija otra regleta: ")
    dibujar_regleta(*regletas[regleta_1])
    dibujar_regleta(*regletas[regleta_2])
    
    
os.system("cls")
preguntar()
# print(">>> REGLETAS <<<")
# dibujar_regleta(1)
# dibujar_regleta(1,2)
# dibujar_regleta(1,3)
# dibujar_regleta(1,4)
# dibujar_regleta(1,5)
# dibujar_regleta(1,6)
# dibujar_regleta(1,8)
# dibujar_regleta(1,10)
# dibujar_regleta(1,12)
