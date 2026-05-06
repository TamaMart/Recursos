# Diagrama de clase 

## Clase trabajador


 ```mermaid
classDiagram
  class trabajador {
    +nombre : str
    -__dinero : int
    +energia : int
    +trabajo : str
    +atributos() void
    +trabajar() void
    +ganancias() void
    +descansar() void
    +get_dinero() int
    +set_dinero(nuevo_dinero : int) void
  }
```
- ¿Que son las relaciones ?

Las relaciones de clase en UML describen cómo se conectan o dependen unas clases con otras.
Hay 4 principales:
1. Herencia 
Una clase hija hereda de una clase padre. Es la relación "es un".
Agricultor --|> trabajador
Un Agricultor es un trabajador.

2. Composición (*--)
Una clase contiene a otra y no puede existir sin ella. Es la relación "tiene un" fuerte.
trabajador *-- Sueldo
Si el trabajador desaparece, el Sueldo también.

3. Agregación (o--)
Una clase usa a otra, pero ambas pueden existir por separado. Es la relación "tiene un" débil.
trabajador o-- Empresa
El trabajador pertenece a una Empresa, pero si la empresa cierra, el trabajador sigue existiendo.

4. Asociación (-->)
Una clase conoce o usa a otra de forma simple.
trabajador --> Producto
El trabajador vende Producto, pero no lo contiene ni lo hereda.

¿Su clase de ejemplo que creo tiene relaciones con otras clases? ¿por qué?

Trabajador es una clase independiente y aislada ya que :

- No hay herencia (class X(trabajador))

- Los atributos son solo str e int, no objetos de otras clases.

- Los métodos no reciben objetos de otras clases como parámetros
  
- Las 3 instancias son de la misma clase, no de clases distintas relacionadas entre sí
