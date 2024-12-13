"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_comencen_per(noms):
    començaC = []
    for e in noms:
        if e[0]== "c" or e[0]=="C":
            començaC.append(e)
    print("Els noms que comencen per C són: {}".format(començaC))
    return començaC
# P principal

noms = llegir_llista()
perA = noms_que_comencen_per(noms)
"""
#Ara el mateix pero comparant la darrera lletra de cada element

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_comencen_per(noms):
    començaC = []
    for e in noms:
        if e[-1]== "e" or e[-1]=="E":
            començaC.append(e)
    print("Els noms que acaben per E són: {}".format(començaC))
    return començaC
# P principal

noms = llegir_llista()
perA = noms_que_comencen_per(noms)