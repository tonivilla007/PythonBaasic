# Crear docuement de text
def crear_llista_fitxer(nom):
    l = []
    with open(nom,"r") as f:
        for line in f:
            l.append(line[:-1])
    return l

#P Principal
l = crear_llista_fitxer("prova1.txt")
print(l)