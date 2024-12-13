"""
Variar l’exercici anterior, perquè enlloc de la lletra a, 
sigui una lletra introduïda per teclat per l’usuari.

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
    lletra = input("Per quina lletra vols que cerqui els noms: ")
    for e in noms:
        if e[0]== lletra.lower() or e[0]== lletra:
            començaC.append(e)
    print("Els noms que comencen per {} són: {}".format(lletra,començaC))
    return començaC
# P principal

noms = llegir_llista()
perA = noms_que_comencen_per(noms)
