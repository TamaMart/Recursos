# Switch Case

A partir de Python 3.10, la estructura match-case funciona como un switch-case tradicional, 
evaluando patrones para ejecutar bloques de código. Si no se cumple ningún caso, se utiliza case _ como opción predeterminada.

* Ejemplo:

``` python
dia = int (input("Ingrese el valor numerico del dia de la semana: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Valor no válido")
        
```
