def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def superposicio(l1, l2):
    ec=[]
    for e in l1:
        if e in l2:
            ec.append(e)
    if len(ec)==0:
        return False, list()
    else:
        return True, ec        
    


# Programa principal
s = llegir_llista()
l = llegir_llista()
hihaec,ec=superposicio(l,s)

if hihaec:
    print("Les dues llistes {} i {} tenen elements en comú i són {}".format(l,s,ec))
else:
    print("Les dues llistes {} i {} no tenen cap element en comú".format(l,s))