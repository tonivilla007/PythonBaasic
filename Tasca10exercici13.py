def menu():
    print("Operacions que pots dur a terme")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Canvi de bases: Decimal a Binari")
    print("6. Canvi de bases: Decimal a Octal")
    print("7. Canvi de bases: Decimal a Hexadecimal")
    print("8. Canvi de bases: Binari a Decimal")
    print("9. Canvi de bases: Binari a Octal")
    print("10. Canvi de bases: Binari a hexadecimal")
    print("11. Canvi de bases: Hexadecimal a decimal")
    print("12. Canvi de bases: Hexadecimal a binari")
    print("13. Canvi de bases: Hexadecimal a octal")
    print("14. Canvi de bases: Octal a Decimal")
    print("15. Canvi de bases: Octal a Binari")
    print("16. Canvi de bases: Octal a Hexadecimal")
    print("17. Sortir")

    op = int(input("Introdueix quina opció vols fer: "))
    return op

def sumar():
    sumant1 = int(input("Diguem el primer sumant: "))
    sumant2 = int(input("Diguem el segon sumant: "))
    resposta = sumant1 + sumant2
    print("{} + {} = {}".format(sumant1, sumant2, resposta))

def restar():
    restant1 = int(input("Diguem el primer restant: "))
    restant2 = int(input("Diguem el segon restant: "))
    resposta = restant1 - restant2
    print("{} - {} = {}".format(restant1, restant2, resposta))

def multiplicar():
    factor1 = int(input("Diguem el primer factor: "))
    factor2 = int(input("Diguem el segon factor: "))
    resposta = factor1 * factor2
    print("{} * {} = {}".format(factor1, factor2, resposta))

def divisio():
    dividend = int(input("Diguem el nombre que vols dividir: "))
    divisor = int(input("Entre quin nombre el vols dividir: "))
    resposta = dividend / divisor
    print("{} / {} = {}".format(dividend, divisor, resposta))

def decimal_a_binari():
    decimal = int(input("Introdueix un nombre decimal: "))
    binari = bin(decimal)[2:]
    print("El nombre binari de {} és {}".format(decimal, binari))

def decimal_a_octal():
    decimal = int(input("Introdueix un nombre decimal: "))
    octal = oct(decimal)[2:]
    print("El nombre octal de {} és {}".format(decimal, octal))

def decimal_a_hexadecimal():
    decimal = int(input("Introdueix un nombre decimal: "))
    hexadecimal = hex(decimal)[2:]
    print("El nombre hexadecimal de {} és {}".format(decimal, hexadecimal))

def binari_a_decimal():
    binari = input("Introdueix un nombre binari: ")
    decimal = int(binari, 2)
    print("El nombre decimal de {} és {}".format(binari, decimal))

def binari_a_octal():
    binari = input("Introdueix un nombre binari: ")
    decimal = int(binari, 2)
    octal = oct(decimal)[2:]
    print("El nombre octal de {} és {}".format(binari, octal))

def binari_a_hexadecimal():
    binari = input("Introdueix un nombre binari: ")
    decimal = int(binari, 2)
    hexadecimal = hex(decimal)[2:]
    print("El nombre hexadecimal de {} és {}".format(binari, hexadecimal))

def hexadecimal_a_decimal():
    hexadecimal = input("Introdueix un nombre hexadecimal: ")
    decimal = int(hexadecimal, 16)
    print("El nombre decimal de {} és {}".format(hexadecimal, decimal))

def hexadecimal_a_binari():
    hexadecimal = input("Introdueix un nombre hexadecimal: ")
    decimal = int(hexadecimal, 16)
    binari = bin(decimal)[2:]
    print("El nombre binari de {} és {}".format(hexadecimal, binari))

def hexadecimal_a_octal():
    hexadecimal = input("Introdueix un nombre hexadecimal: ")
    decimal = int(hexadecimal, 16)
    octal = oct(decimal)[2:]
    print("El nombre octal de {} és {}".format(hexadecimal, octal))

def octal_a_decimal():
    octal = input("Introdueix un nombre octal: ")
    decimal = int(octal, 8)
    print("El nombre decimal de {} és {}".format(octal, decimal))

def octal_a_binari():
    octal = input("Introdueix un nombre octal: ")
    decimal = int(octal, 8)
    binari = bin(decimal)[2:]
    print("El nombre binari de {} és {}".format(octal, binari))

def octal_a_hexadecimal():
    octal = input("Introdueix un nombre octal: ")
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)[2:]
    print("El nombre hexadecimal de {} és {}".format(octal, hexadecimal))

a = True
while a:
    op = menu()
    match op:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            divisio()
        case 5:
            decimal_a_binari()
        case 6:
            decimal_a_octal()
        case 7:
            decimal_a_hexadecimal()
        case 8:
            binari_a_decimal()
        case 9:
            binari_a_octal()
        case 10:
            binari_a_hexadecimal()
        case 11:
            hexadecimal_a_decimal()
        case 12:
            hexadecimal_a_binari()
        case 13:
            hexadecimal_a_octal()
        case 14:
            octal_a_decimal()
        case 15:
            octal_a_binari()
        case 16:
            octal_a_hexadecimal()
        case 17:
            a = False
            print("Adéu, gràcies per emprar la calculadora.")
        case _:
            print("Opció no válida")

         
      
            
        
        