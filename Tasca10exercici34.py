
def contar_vocals(p):
    ap = [0,0,0,0,0]
    for e in p:
        if e == "A" or e == "a":
            ap[0]+=1
        elif e == "e" or e == "E":
            ap[1]+=1
        elif e == "i" or e =="I":
            ap[2]+=1
        elif e == "o" or e =="O":
            ap[3]+=1
        elif e == "u" or e == "U":
            ap[4]+=1
        else:
            print("{} no es una vocal".format(e))
    print("La vocal a apareix {}-vegades la vocal e apareix {}-vegades, la vocal i apareix {}-vegdaes, la vocal o apareix {}-vegades, la vocal u apareix {}-vegades".format(ap[0],ap[1],ap[2],ap[3],ap[4]))

x = input("Introdueix una paraula: ")
contar_vocals(x)