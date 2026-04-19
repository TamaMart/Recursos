#Creacion de un personaje en Python

# Atributos: nombre, fuerza, inteligencia, defensa, vida (se le asigna un valor por defecto a cada uno)
class Personaje:
    nombre = "Default"   
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

# Para darle un valor a los atributos, se utiliza el metodo __init__ (constructor) que se ejecuta automaticamente al crear un objeto de la clase.
# Self es un argumento que hace referencia al objeto que se esta creando, es decir, al personaje que se esta creando. 
# Es necesario para acceder a los atributos y metodos de la clase.
# Un método en Python es una función que pertenece a un objeto o a una clase. Se llama usando un punto (.) después del objeto.

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.__nombre = nombre  # el nombre del personaje se asigna al atributo nombre del objeto que se esta creando.
        self.__fuerza = fuerza  # el valor de fuerza se asigna al atributo fuerza del objeto que se esta creando.
        self.__inteligencia = inteligencia # el valor de inteligencia se asigna al atributo inteligencia del objeto que se esta creando.
        self.__defensa = defensa # el valor de defensa se asigna al atributo defensa del objeto que se esta creando.
        self.__vida = vida # el valor de vida se asigna al atributo vida del objeto que se esta creando.

# Ahora necesita que le pasemos los atributos especificados que va a recibir el personaje al momento de ser creado, para eso se le pasan como argumentos al constructor __init__.
    def atributos(self): # este metodo se encarga de mostrar los atributos del personaje. (con self se accede a los atributos del objeto que se esta creando)
        print(self.__nombre, ":", sep="") # el nombre del personaje se imprime seguido de dos puntos, sin espacio entre ellos (sep="")
        print("Fuerza:", self.__fuerza) # la fuerza del personaje se imprime con el texto "Fuerza:" antes de su valor.
        print("Inteligencia:", self.__inteligencia) # la inteligencia del personaje se imprime con el texto "Inteligencia:" antes de su valor.
        print("Defensa:", self.__defensa) # la defensa del personaje se imprime con el texto "Defensa:" antes de su valor.
        print("Vida:", self.__vida) # la vida del personaje se imprime con el texto "Vida:" antes de su valor.

# Para subir de nivel, el personaje necesita aumentar sus atributos, para eso se crea el metodo subir_nivel que recibe como argumentos los valores que se van a sumar a cada atributo.
    def subir_nivel(self,fuerza, inteligencia, defensa): # este metodo se encarga de subir de nivel al personaje, sumando los valores recibidos como argumentos a los atributos correspondientes del personaje.
        self.__fuerza = self.__fuerza + fuerza # la fuerza del personaje se actualiza sumando el valor recibido como argumento al valor actual de la fuerza del personaje.
        self.__inteligencia + inteligencia # la inteligencia del personaje se actualiza sumando el valor recibido como argumento al valor actual de la inteligencia del personaje.
        self.__defensa + defensa # la defensa del personaje se actualiza sumando el valor recibido como argumento al valor actual de la defensa del personaje.

# Metodo que devuelva un valor booleano que se encarga de verificar si el personaje esta vivo o muerto, para eso se verifica si la vida del personaje es mayor a 0, si es asi, el personaje esta vivo, de lo contrario, el personaje esta muerto.
    def esta_vivo(self): # nombre del metodo que se encarga de verificar si el personaje esta vivo o muerto. Self es un argumento que hace referencia al objeto que se esta creando, es decir, al personaje que se esta creando.
        return self.__vida > 0 # el metodo devuelve un valor booleano que indica si la vida del personaje es mayor a 0, lo que significa que el personaje esta vivo.
    
# Este metodo se encarga de matar al personaje, para eso se le asigna el valor 0 a su atributo vida y se imprime un mensaje indicando que el personaje ha muerto.
    def morir(self): 
        self.__vida = 0  # la vida del personaje se asigna el valor 0, lo que significa que el personaje esta muerto.
        print(self.__nombre, "ha muerto") # se imprime un mensaje indicando que el personaje ha muerto, utilizando el nombre del personaje para personalizar el mensaje.

# Metodo que se encarga de calcular el daño que un personaje le hace a otro, para eso se resta la defensa del enemigo a la fuerza del personaje atacante.
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa # el metodo devuelve el valor del daño que el personaje atacante le hace al enemigo, calculado restando la defensa del enemigo a la fuerza del personaje atacante.
    
# Metodo que se encarga de atacar a otro personaje, para eso se calcula el daño que el personaje atacante le hace al enemigo utilizando el metodo daño, luego se resta ese daño a la vida del enemigo y se imprime un mensaje indicando el ataque realizado y la vida restante del enemigo. Si la vida del enemigo es menor o igual a 0, se llama al metodo morir del enemigo para indicar que ha muerto.    
    def atacar(self, enemigo): # se llama al parsonaje atacante y al enemigo como argumentos del metodo atacar.
        daño = self.daño(enemigo) # se calcula el daño que el personaje atacante le hace al enemigo utilizando el metodo daño, pasando el enemigo como argumento.
        enemigo.__vida = enemigo.__vida - daño # cambiamo la vida del enemigo restando el daño calculado a su vida actual.
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre) #inprimimos un mensaje indicando el ataque realizado, utilizando el nombre del personaje atacante, el daño calculado y el nombre del enemigo para personalizar el mensaje.
        if enemigo.esta_vivo(): # se verifica si el enemigo esta vivo utilizando el metodo esta_vivo del enemigo, si es asi, se imprime un mensaje indicando la vida restante del enemigo.
          print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
        else: # si el enemigo no esta vivo, se llama al metodo morir del enemigo para indicar que ha muerto.
            enemigo.__morir()

# Encapsulamiento: es una tecnica de programacion orientada a objetos que consiste en ocultar los atributos y metodos de una clase para protegerlos de ser modificados o accedidos directamente desde fuera de la clase. 
# En Python, se puede lograr el encapsulamiento utilizando el doble guion bajo (__) antes del nombre de un atributo o metodo, lo que hace que ese atributo o metodo sea privado y no pueda ser accedido directamente desde fuera de la clase. 
# En este ejemplo, se ha encapsulado los atributos del personaje utilizando el doble guion bajo, lo que significa que esos atributos no pueden ser accedidos directamente desde fuera de la clase, sino que solo pueden ser accedidos a través de los metodos de la clase.
# get y set: son metodos que se utilizan para acceder y modificar los atributos encapsulados de una clase. El metodo get se utiliza para devolver el valor de un atributo encapsulado, mientras que el metodo set se utiliza para modificar el valor de un atributo encapsulado.   
    def get_fuerza(self): # este metodo se encarga de devolver el valor de la fuerza del personaje, ya que el atributo fuerza esta encapsulado y no puede ser accedido directamente desde fuera de la clase.
        return self.__fuerza # el metodo devuelve el valor de la fuerza del personaje, accediendo al atributo encapsulado utilizando el doble guion bajo.   
    def set_fuerza(self, fuerza): # este metodo se encarga de modificar el valor de la fuerza del personaje, ya que el atributo fuerza esta encapsulado y no puede ser modificado directamente desde fuera de la clase.
        self.__fuerza = fuerza # el metodo modifica el valor de la fuerza del personaje, accediendo al atributo encapsulado utilizando el doble guion bajo y asignandole el nuevo valor recibido como argumento.    
        if fuerza < 0: # se verifica si el nuevo valor de la fuerza es menor a 0, si es asi, se asigna el valor 0 a la fuerza del personaje para evitar que tenga un valor negativo.
            print ("Error, has introducido un valor negativo") # se imprime un mensaje indicando que la fuerza no puede ser negativa y que se asigna el valor 0 a la fuerza del personaje.
        else:
            self.__fuerza = fuerza # si el nuevo valor de la fuerza es mayor o igual a 0, se asigna ese valor a la fuerza del personaje utilizando el atributo encapsulado con el doble guion bajo.

mi_personaje = Personaje("Tama", 10, 8, 6, 100)  #Creacion del personaje (objeto) con los atributos especificados (nombre, fuerza, inteligencia, defensa, vida)
mi_enemigo =Personaje("Enemigo", 8, 6, 4, 5 ) #Creacion del enemigo (objeto) con los atributos especificados (nombre, fuerza, inteligencia, defensa, vida)

mi_personaje.set_fuerza(15) # se modifica el valor de la fuerza del personaje utilizando el metodo set_fuerza, pasando el nuevo valor como argumento.  
print("La fuerza de", mi_personaje._Personaje__nombre, "es", mi_personaje.get_fuerza()) # se imprime el valor de la fuerza del personaje utilizando el metodo get_fuerza, accediendo al nombre del personaje utilizando el atributo encapsulado con el doble guion bajo.
mi_personaje.atributos() # se llama al metodo atributos del personaje para mostrar sus atributos.



