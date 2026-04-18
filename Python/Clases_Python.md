# Creacion de un personaje en Python

```python
# Atributos: nombre, fuerza, inteligencia, defensa, vida (se le asigna un valor por defecto a cada uno)
class Personaje:
    nombre = "Default"   
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
```
Para darle un valor a los atributos, se utiliza el metodo **__init__ (constructor)**  que se ejecuta automaticamente al crear un objeto de la clase.
**Self** es un argumento que hacer referencia al objeto que se esta creando, es decir, al personaje que se esta creando. 
Es necesario para acceder a los atributos y metodos de la clase.

```python
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre  # el nombre del personaje se asigna al atributo nombre del objeto que se esta creando.
        self.fuerza = fuerza  # el valor de fuerza se asigna al atributo fuerza del objeto que se esta creando.
        self.inteligencia = inteligencia # el valor de inteligencia se asigna al atributo inteligencia del objeto que se esta creando.
        self.defensa = defensa # el valor de defensa se asigna al atributo defensa del objeto que se esta creando.
        self.vida = vida # el valor de vida se asigna al atributo vida del objeto que se esta creando.
 
mi_personaje = Personaje("Tama", 10, 8, 6, 100)  #Creacion del personaje (objeto) con los atributos especificados (nombre, fuerza, inteligencia, defensa, vida)
```
