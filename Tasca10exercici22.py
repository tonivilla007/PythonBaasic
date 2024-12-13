def crear_repetits(n,c):
    return c*n

#Programa principal

a = input("Introdueix un caracter: ")
b = int(input("Introdueix el nombre de vegades que vols que es repeteixi el caracter anterior: "))
print("El caracter {} repetit {} vegades és {}".format(a,b,crear_repetits(b,a)))
