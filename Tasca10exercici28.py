"""
Definir una funció que donada una cadena, avaluï quantes lletres majúscules hi ha. Prova-la amb diferents exemples.
"""

def num_majuscules(s):
    num=0
    j=[]
    for e in s:
      if e.isupper():
        num+=1
        j.append(e)
    return num,"".join(j) 

#Programa principal
a = input("Introdeix una paraula amb minuscules i majiscules: ")
x,y=num_majuscules(a)
print("El número de majuscules que la paraula {} es de {} i són {}".format(a,x,y)) 