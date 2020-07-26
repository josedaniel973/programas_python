# Programa para jugar piedra, papel y tijeras.
print("¡Bienvenido al juego de piedra, papel y tijeras!")
import juego_mod
import random as al
rou = int(input("¿Cuántas rondas quieres jugar? "))
print("Bien, recuerda que:\n1. Piedra\n2.Papel\n3.Tijeras\n")
ref = {1: "piedra", 2: "papel", 3: "tijeras"}
k = 0
while k != rou:
    k += 1
    chs = int(input("Ronda " + str(k) + "!\nEscoge tu movimiento: "))
    print("Has escogido " + ref[chs] + ".")
    comp = al.randint(1, 3)
    if chs == comp:
        print("El rival también escogió " + ref[chs] + ", es un empate.\n")
    elif chs != comp:
        print(juego_mod.pos(chs, comp))
print("Tu puntaje final es de " + str(juego_mod.pts_yo) + ", mientras que el de el rival es de " + str(juego_mod.pts_riv) + ".\n")
if juego_mod.pts_yo > juego_mod.pts_riv:
    print("¡Felicidades! ¡Has Ganado!\n")
elif juego_mod.pts_yo < juego_mod.pts_riv:
    print("Has perdido, mejor suerte la próxima vez.\n")
else:
    print("Han empatado.\n")
print("¡Gracias por jugar!")