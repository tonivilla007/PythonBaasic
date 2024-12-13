"""
x = int(input("Esccriu el menor: "))
y = int(input("Escriu el major: "))
suma = 0

for i in range(x,y+1,1):
    suma+=i
print(suma)
"""

x = int(input("Esccriu el menor: "))
y = int(input("Escriu el major: "))
suma = 0

for i in range(x,y+1,1):
    if i%2==0:
        suma+=i
print(suma)

