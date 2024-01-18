print ("DIVISOR DE NÚMEROS")

dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if divisor == 0:
    print("No se puede dividir por cero.")

cociente = dividendo / divisor
resto = dividendo % divisor

if cociente >= resto:
    print(f"la divicion es exacata. Cociente {cociente}")
else:
    print(f"La división no es exacta. Cociente: {cociente}, Resto: {resto}")