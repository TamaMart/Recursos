#3 Comparación de dos números
#Pide dos números y muestra cuál es mayor o si ambos son iguales.

print("Comparacion de dos numeros")

num1 = int (input("Ingrese primer numero: "))
num2 = int (input("Ingrese segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor")
elif num1 == num2:
    print(f"El numero {num1} y el numero {num2} son iguales")
else:
    print(f"El numero {num2} es mayor")
