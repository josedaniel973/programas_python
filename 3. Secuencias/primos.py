# Algoritmo para buscar números primos.
import random as al
prim = []
num = al.randint(2,10000)
print("El número seleccionado fue " + str(num) + "\nBuscando números primos...")
k = num
while k != 1:
   divs = [str(n) for n in range(1,num) if k % n == 0]
   if len(divs) == 2:
       prim.append(divs[1])
   k -=1
print("Los números primos del 1 al " + str(num) + " son " + str(", ".join(prim[::-1])))
