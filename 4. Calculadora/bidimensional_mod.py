def gon(geom):
    if geom.upper() == "K":
        lado = float(input("Ingresa la magnitud de un lado del cuadrado: "))
        return "%.3f" % (lado ** 2)
    elif geom.upper() == "R":
        base, altura = input("Ingresa la base y la altura: ").split(",")
        base, altura = float(base), float(altura)
        return "%.3f" % (base * altura)
    elif geom.upper() == "C":
        from math import pi
        radio = float(input("¿Cuánto vale el radio? "))
        return "%.3f" % (pi * (radio ** 2))
    elif geom.upper() == "T":
        mtd = input("¿Calcular área por trigonometría o no? S/N ")
        if mtd.upper() == "S":
            from math import sin, radians
            a, b, c = input("Ingresa los valores de 2 lados, y el ángulo en grados del tercero: ").split(",")
            a, b, c = float(a), float(b), float(c)
            return "%.3f" % (0.5 * a * b * sin(radians(c)))
        elif mtd.upper() == "N":
            base, altura = input("Ingresa la base y la altura: ").split(",")
            base, altura = float(base), float(altura)
            return "%.3f" % (base * altura * 0.5)
        else:
            print(mtd.upper() + " no es una opción válida.")
    elif geom.upper() == "P":
        lado = float(input("Escribe el valor de un lado del pentángono: "))
        return "%.3f" % ((lado ** 2) * 0.25 * ((5 * (5 + 2 * (5 ** 0.5))) ** 0.5))
    else:
        print(geom.upper() + " no es una opción válida.")