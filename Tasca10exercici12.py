def menu():
   
        print("Operacions que pots dur a terme")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicació")
        print("4. Divisió")
        print("5. Sortir")

        op = int(input("Introdueix quina opció fols fer: "))
        return op 

def sumar():
    sumant1 = int(input("Diguem el primer sumant: "))
    sumant2 = int(input("Diguem el segon sumant: "))
    resposta = sumant1 + sumant2
    print("{} + {} = {}".format(sumant1,sumant2,resposta))


def restar():
    restant1 = int(input("Diguem el primer restant: "))
    restant2 = int(input("Diguem el segon restant: "))
    resposta = restant1 - restant2
    print("{} - {} = {}".format(restant1,restant2,resposta))

def multiplicar():
    factor1 = int(input("Diguem el primer factor: "))
    factor2 = int(input("Diguem el segon factor: "))
    resposta = factor1 * factor2
    print("{} * {} = {}".format(factor1,factor2,resposta))

def divisio():
    dividend = int(input("Diguem el nombre que vols dividir: "))
    divisor = int(input("Entre quin nombre el vols dividir: "))
    resposta = dividend / divisor
    print("{} / {} = {}".format(dividend,divisor,resposta))


a = True
while a:
    op = menu()
    match (op):
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            divisio()
        case 5:
            a = False
            print("Adéu, gràcies per emprar la calculadora.")
        case _:
            print("Opció no válida")
         
      
            
        
        