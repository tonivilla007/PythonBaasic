x = input("Diguis la primera paraula ")
y = input("Diguis la segona paraula: ")

if x[-3:] == y [-3:]:
    print("Si rimen")
elif x[-2:]== y [-2::]:
    print("Rimen un poc")
    
else:
    print("No rimen")