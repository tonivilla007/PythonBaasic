"""
Escriure un programa que si li introduïm un número menor de 100, 
mostri la suma dels quadrats dels números que estan separats entre sí per a quatres posicions.
 Ex: 80 --> 76**2 + 72**2 + 68**2 + ... 
"""

x = int(input("Intro un num menor 100: "))
y = 0.0
for i in range(x-4,1,-4):
    y += i**2
    print(i)
print("La suma dels quadrats de 4 en quatre de {} és {}".format(x, y))