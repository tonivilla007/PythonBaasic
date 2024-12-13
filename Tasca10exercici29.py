"""
Escriure un programa que converteixi el números binaris en enters
"""

def binadec(b):
    return int(b,2)

#Programa principal

a = input("Introdueix el numero en BINARI (nomes 0 i 1): ")
print("El decimal del binari: {} és {}".format(a,binadec(a)))