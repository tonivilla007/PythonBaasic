# Suma digitis y siu si es parell o no
x = input("Intro un num: ")
sum=0
for e in x:
    sum+=int(e)
if sum%2==0:
    print("La suma dels digits del numero {} és {} i és parell".format(x,sum))
else:
    print("La suma dels digits del numero {} és {} i és senar".format(x,sum))