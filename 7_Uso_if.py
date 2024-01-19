print("COMPROBADOR DE AÑOS BISIESTOS")
año = int(input("Escriba un año y le diré si es bisiesto: "))
if año % 4 == 0 and año % 100 !=0:
    print(f"El año {año} es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.")
elif año % 400 == 0:
    print(f"El año {año} es un año bisiesto porque es múltiplo de 400.")
else:
    print(f"El año {año} no es un año bisiesto.")