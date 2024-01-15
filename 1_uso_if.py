print ("Ingrese los numeros pares o impares")

error = False

numero1 = int(input("Escriba un numero par: "))
numero2 = int(input("Escriba un numero impar: "))

if numero1 % 2 != 0:
    print("No ha escrito un numero par")
    error = True

if numero2 % 2 == 0:
    print("No ha escrito un numero impar.")
    error = True

if error:
    print("Ejecute de nuevo el programa para volver a intentarlo.")

else:
    print("Gracias por su colaboracion.")

