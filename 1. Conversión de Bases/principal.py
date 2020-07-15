#Programa para convertir de decimal a binario y viceversa.
tipo= input('Selecciona "B" si el número a ingresar es base 2,\n"D" si el número a ingresar es base 10,\no "Q" para terminar.\n> ')
tipo=tipo.upper()
while tipo != "Q":
    if tipo == "B":
        num= str(input("Ingresa tu número en base binaria: "))
        import decimal_mod
        num= decimal_mod.dec(num)
        print("El número resultante es " + str(num) + ".\n")
        tipo = input('Selecciona "B" si el número a ingresar es base 2,\n"D" si el número a ingresar es base 10,\no "Q" para terminar.\n> ')
        tipo = tipo.upper()
    elif tipo == "D":
        num= int(input("Ingresa tu número en base decimal: "))
        if num == 0:
            print("El número resultante es " + str(num) + ".\n")
        else:
            import binario_mod
            num= binario_mod.bin(num)
            print("El número resultante es " + str(num) + ".\n")
        tipo = input('Selecciona "B" si el número a ingresar es base 2,\n"D" si el número a ingresar es base 10,\no "Q" para terminar.\n> ')
        tipo = tipo.upper()
    else:
        tipo= input('Selecciona "B", "D", o "Q"\n> ')
        tipo= tipo.upper()
print("Proceso terminado.")