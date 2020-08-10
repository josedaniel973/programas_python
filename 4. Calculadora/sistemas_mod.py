def lin():
    print("Considera tres igualdades del tipo Ax + By + Cz = D")
    x1, y1, z1, r1 = input("Escribe los valores de los coeficientes de la primera igualdad: ").split(",")
    x2, y2, z2, r2 = input("Escribe los valores de los coeficientes de la segunda igualdad: ").split(",")
    x3, y3, z3, r3 = input("Escribe los valores de los coeficientes de la tercera igualdad: ").split(",")
    x1, x2, x3, y1, y2, y3, z1, z2, z3, r1, r2, r3 = float(x1), float(x2), float(x3), float(y1), float(y2), float(y3), float(z1), float(z2), float(z3), float(r1), float(r2), float(r3)
    prx = float(((r1 * y2 * z3) + (y1 * z2 * r3) + (z1 * r2 * y3)) - ((y1 * r2 * z3) + (r1 * z2 * y3) + (z1 * y2 * r3)))
    pry = float(((x1 * r2 * z3) + (x2 * r3 * z1) + (x3 * r1 * z2)) - ((z1 * r2 * x3) + (z2 * r3 * x1) + (z3 * r1 * x2)))
    prz = float(((x1 * y2 * r3) + (y1 * r2 * x3) + (r1 * x2 * y3)) - ((r1 * y2 * x3) + (x1 * r2 * y3) + (y1 * x2 * r3)))
    prr = float(((x1 * y2 * z3) + (x2 * y3 * z1) + (x3 * y1 * z2)) - ((z1 * y2 * x3) + (z2 * y3 * x1) + (z3 * y1 * x2)))
    xres, yres, zres = (prx / prr), (pry / prr), (prz / prr)
    return "\nEl valor de 'x' es " + "%.2f" % xres + ", el valor de 'y' es " + "%.2f" % yres + ", y el valor de 'z' es " + "%.2f" % zres + "."
