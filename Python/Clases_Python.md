# Creacion de un personaje en Python

[Personaje](Personaje.py)

```python
# Atributos: nombre, fuerza, inteligencia, defensa, vida (se le asigna un valor por defecto a cada uno)
class Personaje:
    nombre = "Default"   
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
```
* Para darle un valor a los atributos, se utiliza el metodo **__init__ (constructor)**  que se ejecuta automaticamente al crear un objeto de la clase.
  
* **Self** es un argumento que hacer referencia al objeto que se esta creando, es decir, al personaje que se esta creando.Es necesario para acceder a los atributos y metodos de la clase.
  
* Un **método** en Python es una función que pertenece a un objeto o a una clase. Se llama usando un punto (.) después del objeto.

```python
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre  # el nombre del personaje se asigna al atributo nombre del objeto que se esta creando.
        self.fuerza = fuerza  # el valor de fuerza se asigna al atributo fuerza del objeto que se esta creando.
        self.inteligencia = inteligencia # el valor de inteligencia se asigna al atributo inteligencia del objeto que se esta creando.
        self.defensa = defensa # el valor de defensa se asigna al atributo defensa del objeto que se esta creando.
        self.vida = vida # el valor de vida se asigna al atributo vida del objeto que se esta creando.
 
mi_personaje = Personaje("Tama", 10, 8, 6, 100)  #Creacion del personaje (objeto) con los atributos especificados (nombre, fuerza, inteligencia, defensa, vida)
```

# Encapsulación

[Personaje encapsulado](personaje_encapsulado.py)

- Encapsulamiento: es una tecnica de programacion orientada a objetos que consiste en ocultar los atributos y metodos de una clase para protegerlos de ser modificados o accedidos directamente desde fuera de la clase. 
En Python, se puede lograr el encapsulamiento utilizando el doble guion bajo (__) antes del nombre de un atributo o metodo, lo que hace que ese atributo o metodo sea privado y no pueda ser accedido directamente desde fuera de la clase. En este ejemplo, se ha encapsulado los atributos del personaje utilizando el doble guion bajo, lo que significa que esos atributos no pueden ser accedidos directamente desde fuera de la clase, sino que solo pueden ser accedidos a través de los metodos de la clase.

-  Get y set: son metodos que se utilizan para acceder y modificar los atributos encapsulados de una clase. El metodo get se utiliza para devolver el valor de un atributo encapsulado, mientras que el metodo set se utiliza para modificar el valor de un atributo encapsulado.


```python

def get_fuerza(self): # este metodo se encarga de devolver el valor de la fuerza del personaje, ya que el atributo fuerza esta encapsulado y no puede ser accedido directamente desde fuera de la clase.
        return self.__fuerza # el metodo devuelve el valor de la fuerza del personaje, accediendo al atributo encapsulado utilizando el doble guion bajo.
def set_fuerza(self, fuerza): # este metodo se encarga de modificar el valor de la fuerza del personaje, ya que el atributo fuerza esta encapsulado y no puede ser modificado directamente desde fuera de la clase.
        self.__fuerza = fuerza # el metodo modifica el valor de la fuerza del personaje, accediendo al atributo encapsulado utilizando el doble guion bajo y asignandole el nuevo valor recibido como argumento.    
        if fuerza < 0: # se verifica si el nuevo valor de la fuerza es menor a 0, si es asi, se asigna el valor 0 a la fuerza del personaje para evitar que tenga un valor negativo.
            print ("Error, has introducido un valor negativo") # se imprime un mensaje indicando que la fuerza no puede ser negativa y que se asigna el valor 0 a la fuerza del personaje.
        else:
            self.__fuerza = fuerza # si el nuevo valor de la fuerza es mayor o igual a 0, se asigna ese valor a la fuerza del personaje utilizando el atributo encapsulado con el doble guion bajo.
```

# Herencia

¿Por qué cuando se crea la clase guerrero al inicio heredando de la clase personaje genera error el código?

- Se necesita inicializar los atributos de personaje
  
¿Cuándo en el video se menciona la super clase a que se refiere?

- Super clase: constructor de la clases de la que hereda
- La funcion super () permite llamar a los atributos y metodos de la supoer clase sin tener que escribirla directamente 











