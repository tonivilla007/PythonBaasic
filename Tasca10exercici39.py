"""
Escriure un programa que calculi en quan s'hauria convertit el nostre capital al final dels anys. 
Per això li hem de demanar a l’usuari que introdueixi la quantitat a sol·licitar 
(mínim 50000€ màxim 800000€), un interès (mínim 0.5% i màxim 13%) i el número d’anys 
(mínim 3 anys - màxim 40 anys). 
 La fórmula per calcular-ho és: Cfinal = Cinicial * (1 + interés/100) **  anys. 
   Ex. 10000€ a 4.5% d’interés a 20 anys s’ha de convertir en 24117.14€
"""

x = int(input("Quantitat: "))
i = float(input("Interés: "))
a = int(input("Número d'anys: "))
c = x * ((1+i/100)**a)
print("Amb el capital {} amb un interés {} per {}-anys, al final es convertirà en un valor de {}".format(x, i, a, c))
