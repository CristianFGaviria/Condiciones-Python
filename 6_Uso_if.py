print("COMPARADOR DE TRES NÚMEROS")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 == numero2 and numero2 == numero3:
    print("Ha escrito tres veces el mismo número.")
elif numero1 == numero2 or numero2 == numero3:
    print("Ha escrito uno de los números dos veces.")
elif numero2 == numero1 or numero3 == numero1:
    print("Ha escrito uno de los números dos veces.")
else:
    print("Los tres números que ha escrito son distintos.")