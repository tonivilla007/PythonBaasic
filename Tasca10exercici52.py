# Identifica la posició
def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Insereix una paraula: ")
        if a != ".":
            l.append(a)
    return l

def index_paraula(l,paraula):
    if paraula not in l:
        return -1
    else:
        for i,e in enumerate(l):
            if e ==paraula:
                return i
            
# P Principal
l = llegir_llista()
p = input("Dir quina paraula de la llista vols cercar: ")
n = index_paraula(l,p)
if n>0:
    print("La paraula {} esá en la posició {}".format(p,n+1))
else:
    print("La paraula no está a la llista")
