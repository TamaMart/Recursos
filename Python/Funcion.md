# FUNCION

Las funciones en Python son bloques de código reutilizables y organizados que realizan una tarea específica, 
definidos con la palabra clave def. Permiten modularizar programas, mejorando la legibilidad y evitando la repetición de código

* Ejemplo:

```python
def puntacion (clase):
    return sum(clase) / len(clase)

clase= [7, 8, 9]
promedio = puntacion(clase)
print("El promedio de la clase es:", promedio)
```
