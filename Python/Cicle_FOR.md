# Ciclo **For**

El ciclo for en Python se utiliza para iterar sobre secuencias (listas, tuplas, diccionarios, cadenas, rangos). Ejecuta un bloque de código indentado para cada elemento de la secuencia. Su sintaxis es: for elemento in secuencia:, seguido del código a repetir, permitiendo automatizar tareas repetitivas de forma eficiente.

* Ejemplo: Iterar sobre una lista
```python
coleccion = {'andres':22, 'tamara': 21, 'maria': 20}
for clave, valor in coleccion.items():
    print(f'{clave} tiene {valor} años')
```
