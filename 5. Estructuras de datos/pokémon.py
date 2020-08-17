import random as al
ref,stats = dict(),dict()
pokémon = ["Mewtwo", "Pikachu", "Gengar", "Charizard", "Blaziken", "Mimikyu",
            "Greninja", "Garchomp", "Decidueye", "Sharpedo", "Wobbufeet",
            "Litten", "Blissey", "Jigglypuff", "Venusaur", "Nidoking",
            "Dragonite", "Gyrados", "Alakazam", "Eevee", "Lucario", "Snorlax",
            "Weavile", "Marowak", "Gardevoir", "Skarmory", "Salamence",
            "Metagross", "Rattata", "Shedinja", "Serperior", "Heracross",
            "Espurr", "Chandelure", "Tauros", "Omanyte", "Hawlucha", "Gliscor",
            "Empoleon", "Yamask", "Scizor", "Slowpoke", "Steelix", "Onix",
            "Glalie", "Arcanine", "Bewear", "Jolteon", "Ditto", "Bidoof",
            "Magcargo", "Azumarill", "Kabutops", "Shuckle", "Sableye",
            "Tyranitar", "Castform", "Porygon", "Mudkip", "Smeargle", "Crobat",
            "Machamp", "Drifloon", "Milotic", "Houndoom", "Togepi", "Rhydon",
            "Electrode", "Altaria", "Magnezone", "Pachirisu"]
mi_equipo = al.sample(pokémon,5)
print("Tus opciones de pokémon iniciales son " + str(", ".join(mi_equipo)) + ".")
for p in range(1,6):
    print(str(p) + ". " + str(mi_equipo[p-1]))
    ref[p] = mi_equipo[p-1]
while len(ref) != 0:
    inpkm = int(input("\nVamos a capturar pokémon! Selecciona un número,\no presiona 0 para salir.\n> "))
    if 0 <= inpkm <= 5:
        if inpkm == 0:
            print("\nGracias por jugar!")
            mi_equipo.clear()
            break
        elif al.randint(1,100) > 61:
            print("\nHas capturado a " + ref[inpkm] + "!")
            lv = al.randint(1,100)
            stats[ref[inpkm]] = str("Nombre: " + ref[inpkm] + "\nVida - " + str((al.randint(5,10)*lv)) + "\nNivel - " + str(lv))
            del ref[inpkm]
        else:
            print("\nLástima, " + ref[inpkm] + " se ha escapado...")
            mi_equipo.remove(ref[inpkm])
            del ref[inpkm]
    else:
        print("\nSelecciona un número válido.")
if len(mi_equipo) == 0 and inpkm != 0:
    print("\nParece que no has capturado a nadie...\nMejor suerte la próxima!")
elif mi_equipo != 0 and inpkm != 0:
    print("\nCapturaste " + str(len(mi_equipo)) + " pokémon:")
    for m in range(1,len(mi_equipo)+1):
        print(str(m) + ". " + str(mi_equipo[m-1]))
    while True:
        selstat = int(input("\nSelecciona un pokémon para ver sus estadísticas,\no presiona 0 para salir.\n> "))
        if selstat == 0:
            print("\nGracias por jugar!")
            break
        elif 0 <= selstat <= m:
            print("\nInformación de " + str(mi_equipo[selstat-1]) + ":")
            print(stats[mi_equipo[selstat-1]])
        else:
            selstat = int(input("\nSelecciona un número válido.\n> "))
