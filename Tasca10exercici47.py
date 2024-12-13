def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix uns nombres: ")
        if a != ".":
            l.append(int(a))
    return l

def esta_ordenada(l):
    ascendent = sorted(l)
    descendent = sorted(l, reverse=True)
    if l == ascendent:
        print("La llista està ordenada de forma ascendent")
    elif l == descendent:
        print("La llista està ordenada de forma descendent")
    else:
        print("La llista no està ordenada")

# P principal
l = llegir_llista()
esta_ordenada(l)
