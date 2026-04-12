# Condicionales 

- **if** es una estructura de control que permite ejecutar un bloque de código si se cumple una condición. En este caso, se pide al usuario que ingrese un número y se verifica si es positivo, negativo o cero.
- **elif** es una estructura de control que se utiliza junto con if para verificar múltiples condiciones. En este caso, se verifica si el número es negativo.
- **else** es una estructura de control que se utiliza junto con if para ejecutar un bloque de código si ninguna de las condiciones anteriores se cumple. En este caso, se ejecuta si el número es cero.
```python
numero = int(input("Ingrese un número: "))

if numero > 0:

    print("El número es positivo.")
   
elif numero < 0:

    print("El número es negativo.")
   
else:

    print("El número es cero.")
