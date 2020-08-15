def dro(geom):
    if geom.upper() == "C":
        lado = float(input("¿Cuánto mide un arista del cubo?"))
        return lado**3
    elif geom.upper() == "N":
        x,y,z = input("Ingresa las medidas del largo y el ancho y la profundidad: ").split(",")
        x,y,z = float(x),float(y),float(z)
        return x*y*z
    elif geom.upper() == "E":
        radio = float(input("Teclea la magnitud del radio de la esfera: "))
        from math import pi
        return (4/3)*pi*(radio**3)
    elif geom.upper() == "V":
        radio,altura = input("Ingresa el radio de la base del cono y su altura: ").split(",")
        radio, altura = float(radio),float(altura)
        from math import pi
        return (1/3)*pi*altura*(radio**2)
    elif geom.upper() == "L":
        radio,altura = input("Ingresa el radio de la base y altura del cilindro: ").split(",")
        radio, altura = float(radio),float(altura)
        from math import pi
        return pi*altura*(radio**2)
