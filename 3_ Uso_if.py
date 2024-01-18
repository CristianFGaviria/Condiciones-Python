print("COMPARADOR DE NÚMEROS")

numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    print(f"Menor: {numero2}; mayor: {numero1}. ")
if numero2 > numero1:
    print(f"Menor: {numero1}; mayor: {numero2}. ")
else:
    print("los dos numeros son iguales. ")

