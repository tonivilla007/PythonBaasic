"""
Escriure un programa on donats l’any actual, i l’any de naixement i el nom de 4 persones, calculi els anys que farà cada un d’ells l’any actual i imprimeixi totes les dades tabulades per pantalla. Ex:
Any actual 2022
Nom			Data naixement	Anys que farà aquest any
Pere			2000			22
Maria			1999			23
Anna			2005			17
"""

a= "2024"
l=[]
for i in range(4):
    d=[]
    d.append(input("Indica el teu nom: "))
    d.append(input("Indica l'any (aaaa) que vas neixer: "))
    l.append(d)
print("{:<20} {:<20} {:<20}".format("Nom", "Data neixament", "Anys que fara aquest any"))

for i in range(4):
     print("{:<20} {:<20} {:<20}".format(l[i][0], l[i][1], int(a) - int(l[i][1])))
