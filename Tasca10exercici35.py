"""
Definir una funció es_de_traspas() donat un any, 
ens indiqui si és de traspàs o no. Un any és de traspàs si és divisible per 4, 
però no per 100 i també és divisible per 400.

"""

def es_de_TRASPAS():
    any = int(input("Introdueix un any: "))
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        print("L'any introduit {} és un any de pas".format(any))
    else:
        print("L'any introduit, {} no es un any de pas".format(any))

# Principal

a = es_de_TRASPAS()