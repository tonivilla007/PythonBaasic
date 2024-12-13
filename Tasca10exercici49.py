"""
Definir una funció llista_20_elements() que retorni una llista de 20 elements 
creats aleatòriament entre 1 i 100. Provar amb la funció anterior si s'han generat elements duplicats o no.
"""
import random

def llista_20_elements():
    l = []
    for i in range(20):
        l.append(random.randint(1,100))
    return l

def hi_ha_duplicats(l):
    s = set(l)
    if len(l)==len(s):
        print("No hi ha duplicats")
    else:
        print("Hi ha duplicats")
    
# P Principal
l = llista_20_elements()
print(l)

j = hi_ha_duplicats(l)