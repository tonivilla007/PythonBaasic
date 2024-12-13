# Invertir una llista
def invertir(s):
    return s[::-1]
s = input("Introduir una cadena: ")
print("La inversa de {} és {}".format(s, invertir(s)))