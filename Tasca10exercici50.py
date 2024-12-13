#Elimina duplicats
def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix uns nombres: ")
        if a != ".":
            l.append(int(a))
    return l

def elimina_duplicats(l):
    s = set(l)
    return list(s)

#P Principal 
l = llegir_llista()
r = elimina_duplicats(l)
print("La llista {} queda així {}".format(l,r))