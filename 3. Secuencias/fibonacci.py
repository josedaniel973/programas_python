# Algoritmo para obtener el n-ésimo número de Fibonacci.
anterior2, anterior1, actual = 0, 0, 1
bus = int(input("Posición del número de fibonacci a buscar: "))
k = bus
if bus == 1 or bus == 2:
    print("Los primer y segundo números de fibonacci son " + str(actual) + ".")
else:
    while bus != 1:
        anterior1 = actual
        actual = anterior1 + anterior2
        anterior2 = anterior1
        bus -= 1
    print("El valor del número de Fibonacci que se encuentra en la posición " + str(k) + " vale " + str(actual) + ".")
