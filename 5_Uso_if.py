print("COMPARADOR DE MÚLTIPLOS")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 >= numero2 and numero1 % numero2 == 0:
    print(f"{numero1} es multiplo de {numero2}")
elif numero1 >= numero2 and numero1 % numero2 != 0:
    print(f"{numero1} no es multiplo de {numero2}")
elif numero2 > numero1 and numero2 % numero1 == 0:
    print(f"{numero2} es multiplo de {numero1}")
else:
    print(f"{numero2} no es multiplo de {numero1}")
