#Módulo para convertir de decimal a binario.
def bin(num):
    res= []
    while num != 0:
        res.append(str(num%2))
        num = num // 2
    res = reversed(res)
    s = ""
    for item in res:
        s += item
    return s


