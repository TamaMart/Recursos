# WHILE 

El bucle **while** en Python repite un bloque de código continuamente mientras una condición sea verdadera (True). 
Se utiliza cuando no se conoce de antemano el número exacto de iteraciones. La condición se evalúa antes de cada iteración, y el bucle termina cuando se vuelve falsa (False).





``` python
contrasena = "meli"
contador= 0
while True:
    contrasena_input= input("Ingrese la contraseña: ")
    contador += 1
    if contador > 3:
        print("Has excedido el número de intentos. Intenta más tarde.")
        break
    elif contrasena_input == 'meli':
        print("Contraseña correcta. ")
        break   
    else:
        print("Contraseña incorrecta. Intente de nuevo.")
```
