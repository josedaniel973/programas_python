def lin():
    x1, y1 = input("\nEscoge las coordenadas 'x' e 'y' respectivamente para el primer punto: ").split(",")
    x2, y2 = input("Escoge las coordenadas 'x' e 'y' respectivamente para el segundo punto: ").split(",")
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    m = float(((y2 - y1) / (x2 - x1)))
    dist = float((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    linea = str("y = " + "%.3f" % m + "x + (" + "%.3f" % ((m * (-x1)) + y1) + ")")
    return "La distancia entre ambos puntos es aprox. " + "%.2f"%dist + " unidades y su ecuación de la recta es:\n" + str(linea)