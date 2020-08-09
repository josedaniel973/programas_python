#Programa para obtener distancias, áreas, volúmenes, derivar, y resolver sistemas de ecuaciones.
print("¡Bienvenido a calculadora!")
opt = input("¿Qué quieres hacer?\nL - Calcular recta que une 2 puntos.\nA - Calcular área de un polígono.\nV - Calcular volumen de un poliedro.\nS - Resolver sistemas de ecuaciones.\nQ - Salir\n> ")
while opt.upper() != "":
    if opt.upper() == "L":
        import recta_mod as rect
        print("\n" + rect.lin())
        opt = input("\n¿Qué sigue?\nD - Calcular recta que une 2 puntos.\nA - Calcular área de un polígono.\nV - Calcular volumen de un poliedro.\nS - Resolver sistemas de ecuaciones.\nQ - Salir\n> ")
        opt = opt.upper()
    elif opt.upper() == "A":
        import bidimensional_mod as bi
        geom = input("\nSelecciona la figura:\nK - Cuadrado\nR - Rectángulo\nC - Círculo\nT - Triángulo\nP - Pentágono\n> ")
        print("El área de la figura es " + bi.gon(geom) + " unidades cuadradas.")
        opt = input("\n¿Qué sigue?\nD - Calcular recta que une 2 puntos.\nA - Calcular área de un polígono.\nV - Calcular volumen de un poliedro.\nS - Resolver sistemas de ecuaciones.\nQ - Salir\n> ")
        opt = opt.upper()
    elif opt.upper() == "V":
        import tridimensional_mod as tri
        geom = input("\nSelecciona la figura:\nC - Cubo\nN - Cuboide\nE - Esfera\nV - Cono\nL - Cilindro\n> ")
        print("El volumen de la figura es " + tri.dro(geom) + " unidades cúbicas.")
        opt = input("\n¿Qué sigue?\nD - Calcular recta que une 2 puntos.\nA - Calcular área de un polígono.\nV - Calcular volumen de un poliedro.\nS - Resolver sistemas de ecuaciones.\nQ - Salir\n> ")
        opt = opt.upper()
    elif opt.upper() == "S":
        print("\nSólo puedes resolver de 3x3.")
        import sistemas_mod as sis
        print(sis.lin())
        opt = input("\n¿Qué sigue?\nD - Calcular recta que une 2 puntos.\nA - Calcular área de un polígono.\nV - Calcular volumen de un poliedro.\nS - Resolver sistemas de ecuaciones.\nQ - Salir\n> ")
        opt = opt.upper()
    elif opt.upper() == "Q":
        print("\nProceso terminado.")
        break
    else:
        opt = input("\nEsa no es una opción válida. Escoge una de las 5 letras.")
        opt= opt.upper()
