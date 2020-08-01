pts_yo, pts_riv = 0, 0
def pos(chs, comp):
    global pts_yo, pts_riv
    ref = {1: "piedra", 2: "papel", 3: "tijeras"}
    if chs == 1:
        if comp == 2:
            pts_riv += 1
            return "El rival escogió " + ref[comp] + ", mala suerte!\nTu rival 1 punto.\n"
        else:
            pts_yo += 1
            return "El rival escogió " + ref[comp] + ", bien!\nObtienes 1 puntos.\n"
    if chs == 2:
        if comp == 3:
            pts_riv += 1
            return "El rival escogió " + ref[comp] + ", mala suerte!\nTu rival obtiene 1 punto.\n"
        else:
            pts_yo += 1
            return "El rival escogió " + ref[comp] + ", bien!\nObtienes 1 punto.\n"
    if chs == 3:
        if comp == 1:
            pts_riv += 1
            return "El rival escogió " + ref[comp] + ", mala suerte!\nTu rival obtiene 1 punto.\n"
        else:
            pts_yo += 1
            return "El rival escogió " + ref[comp] + ", bien!\nObtienes 1 punto.\n"
