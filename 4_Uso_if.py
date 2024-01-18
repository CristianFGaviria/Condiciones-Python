print("COMPARADOR DE AÑOS")
año1 = int(input("¿En qué año estamos?: "))
año2 = int(input("Escriba un año cualquiera: "))
resultado = año2 -año1

if año1 < año2 and año2 - año1 == 1:
    print(f"Para llegar al año {año2} faltan {resultado} año.")
elif  año1 < año2:
    print(f"Para llegar al año {año2} faltan {resultado} años.")
elif año1 > año2:
    resultante = año1 - año2
    print(f"Desde el año {año2} han pasado {resultante} años.")
else:
    print("¡Son el mismo año!")