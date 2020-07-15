# Módulo para convertir de binario a decimal.
def dec(num):
    num= [int(x) for x in str(num)]
    pot = [2 ** j for j in range(0, (len(num)))][::-1]
    ref = list(zip(num, pot))
    mult = [((ref[k][0]) * (ref[k][1])) for k in range(0, len(num))]
    return sum(mult)
