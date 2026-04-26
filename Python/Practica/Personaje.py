#Creacion de un personaje en Python

# Atributos: nombre, fuerza, inteligencia, defensa, vida (se le asigna un valor por defecto a cada uno)
class Personaje:
    nombre = "Default"   
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

# Para darle un valor a los atributos, se utiliza el metodo __init__ (constructor) que se ejecuta automaticamente al crear un objeto de la clase.
# Self es un argumento que hacer referencia al objeto que se esta creando, es decir, al personaje que se esta creando. 
# Es necesario para acceder a los atributos y metodos de la clase.

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre  # el nombre del personaje se asigna al atributo nombre del objeto que se esta creando.
        self.fuerza = fuerza  # el valor de fuerza se asigna al atributo fuerza del objeto que se esta creando.
        self.inteligencia = inteligencia # el valor de inteligencia se asigna al atributo inteligencia del objeto que se esta creando.
        self.defensa = defensa # el valor de defensa se asigna al atributo defensa del objeto que se esta creando.
        self.vida = vida # el valor de vida se asigna al atributo vida del objeto que se esta creando.
      
# Ahora necesita que le pasemos los atributos especificados que va a recibir el personaje al momento de ser creado, para eso se le pasan como argumentos al constructor __init__.
    def atributos(self): # este metodo se encarga de mostrar los atributos del personaje. (con self se accede a los atributos del objeto que se esta creando)
        print(self.nombre, ":", sep="") # el nombre del personaje se imprime seguido de dos puntos, sin espacio entre ellos (sep="")
        print("Fuerza:", self.fuerza) # la fuerza del personaje se imprime con el texto "Fuerza:" antes de su valor.
        print("Inteligencia:", self.inteligencia) # la inteligencia del personaje se imprime con el texto "Inteligencia:" antes de su valor.
        print("Defensa:", self.defensa) # la defensa del personaje se imprime con el texto "Defensa:" antes de su valor.
        print("Vida:", self.vida) # la vida del personaje se imprime con el texto "Vida:" antes de su valor.

# Para subir de nivel, el personaje necesita aumentar sus atributos, para eso se crea el metodo subir_nivel que recibe como argumentos los valores que se van a sumar a cada atributo.
    def subir_nivel(self,fuerza, inteligencia, defensa): # este metodo se encarga de subir de nivel al personaje, sumando los valores recibidos como argumentos a los atributos correspondientes del personaje.
        self.fuerza = self.fuerza + fuerza # la fuerza del personaje se actualiza sumando el valor recibido como argumento al valor actual de la fuerza del personaje.
        self.inteligencia + inteligencia # la inteligencia del personaje se actualiza sumando el valor recibido como argumento al valor actual de la inteligencia del personaje.
        self.defensa + defensa # la defensa del personaje se actualiza sumando el valor recibido como argumento al valor actual de la defensa del personaje.

# Metodo que devuelva un balor booleano que se encarga de verificar si el personaje esta vivo o muerto, para eso se verifica si la vida del personaje es mayor a 0, si es asi, el personaje esta vivo, de lo contrario, el personaje esta muerto.
    def esta_vivo(self): # nombre del metodo que se encarga de verificar si el personaje esta vivo o muerto. Self es un argumento que hace referencia al objeto que se esta creando, es decir, al personaje que se esta creando.
        return self.vida > 0 # el metodo devuelve un valor booleano que indica si la vida del personaje es mayor a 0, lo que significa que el personaje esta vivo.
    
# Este metodo se encarga de matar al personaje, para eso se le asigna el valor 0 a su atributo vida y se imprime un mensaje indicando que el personaje ha muerto.
    def morir(self): 
        self.vida = 0  # la vida del personaje se asigna el valor 0, lo que significa que el personaje esta muerto.
        print(self.nombre, "ha muerto") # se imprime un mensaje indicando que el personaje ha muerto, utilizando el nombre del personaje para personalizar el mensaje.

# Metodo que se encarga de calcular el daño que un personaje le hace a otro, para eso se resta la defensa del enemigo a la fuerza del personaje atacante.
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa # el metodo devuelve el valor del daño que el personaje atacante le hace al enemigo, calculado restando la defensa del enemigo a la fuerza del personaje atacante.
    
# Metodo que se encarga de atacar a otro personaje, para eso se calcula el daño que el personaje atacante le hace al enemigo utilizando el metodo daño, luego se resta ese daño a la vida del enemigo y se imprime un mensaje indicando el ataque realizado y la vida restante del enemigo. Si la vida del enemigo es menor o igual a 0, se llama al metodo morir del enemigo para indicar que ha muerto.    
    def atacar(self, enemigo): # se llama al parsonaje atacante y al enemigo como argumentos del metodo atacar.
        daño = self.daño(enemigo) # se calcula el daño que el personaje atacante le hace al enemigo utilizando el metodo daño, pasando el enemigo como argumento.
        enemigo.vida = enemigo.vida - daño # cambiamo la vida del enemigo restando el daño calculado a su vida actual.
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre) #inprimimos un mensaje indicando el ataque realizado, utilizando el nombre del personaje atacante, el daño calculado y el nombre del enemigo para personalizar el mensaje.
        if enemigo.esta_vivo(): # se verifica si el enemigo esta vivo utilizando el metodo esta_vivo del enemigo, si es asi, se imprime un mensaje indicando la vida restante del enemigo.
          print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else: # si el enemigo no esta vivo, se llama al metodo morir del enemigo para indicar que ha muerto.
            enemigo.morir()

mi_personaje = Personaje("Tama", 10, 8, 6, 100)  #Creacion del personaje (objeto) con los atributos especificados (nombre, fuerza, inteligencia, defensa, vida)
mi_enemigo =Personaje("Enemigo", 8, 6, 4, 5 ) #Creacion del enemigo (objeto) con los atributos especificados (nombre, fuerza, inteligencia, defensa, vida)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
