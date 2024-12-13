
"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors_que(t,min,max):
    for e in t:
        if e>min and e<max:
            print("{} esta entre {} i {}".format(e,min,max))
        
#P principal

x = llegir_llista()
y = tuple(x)
min=int(input("Introdueix el numero petit a comparar: "))
max=int(input("Introdueix el numero gran a comparar: "))
mostrar_majors_que(y, min, max)
"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors_que(t,min,max):
    print("Els numeros entre aquets dos són: {}".format(list(filter(lambda x: x>min and x<max,t))))

#P principal

x = llegir_llista()
y = tuple(x)
min=int(input("Introdueix el numero petit a comparar: "))
max=int(input("Introdueix el numero gran a comparar: "))
mostrar_majors_que(y, min, max)