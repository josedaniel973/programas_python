# Programa para jugar piedra, papel y tijeras.

import random as al
chs = int(input("Selecciona piedra, papel, o tijeras.\n1.- Papel\n2.- Piedra\n3.- Tijeras\n> "))
ref= {1:"papel",2:"piedra",3: "tijeras"}
if 0 < chs < 4:
    print("Has escogido " + ref[chs] + ".")
    comp = int(al.randint(1, 3))
    while comp == chs:
        print("Computadora también escogió " + ref[comp] + ", es un empate.")
        chs = int(input("\nSelecciona piedra, papel, o tijeras.\n1.- Papel\n2.- Piedra\n3.- Tijeras\n> "))
        print("Has escogido " + ref[chs] + ".")
        comp = al.randint(1, 3)
    if comp == 3:
        if chs == 1:
            print("Computadora escogió " + ref[comp] + ", perdiste!")
        elif chs == 2:
            print("Computadora escogió " + ref[comp] + ", ganaste!")
    elif comp == 2:
        if chs == 1:
            print("Computadora escogió " + ref[comp] + ", ganaste!")
        elif chs == 3:
            print("Computadora escogió " + ref[comp] + ", perdiste!")
    elif comp == 1:
        if chs == 3:
            print("Computadora escogió " + ref[comp] + ", ganaste!")
        elif chs == 2:
            print("Computadora escogió " + ref[comp] + ", perdiste!")
else:
    print("No es una opción válida.")
