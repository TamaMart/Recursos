class Personaje:

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self._nombre = nombre  
        self._fuerza = fuerza  
        self._inteligencia = inteligencia
        self._defensa = defensa 
        self._vida = vida 


    def atributos(self): 
        print(self._nombre, ":", sep="") 
        print("Fuerza:", self._fuerza) 
        print("Inteligencia:", self._inteligencia) 
        print("Defensa:", self._defensa) 
        print("Vida:", self._vida) 


    def subir_nivel(self,fuerza, inteligencia, defensa): 
        self._fuerza = self._fuerza + fuerza 
        self._inteligencia += inteligencia 
        self._defensa += defensa 

    def esta_vivo(self): 
        return self._vida > 0
    

    def morir(self): 
        self._vida = 0  
        print(self._nombre, "ha muerto")

    def daño(self, enemigo):
        return self._fuerza - enemigo._defensa 
    
  
    def atacar(self, enemigo): 
        daño = self.daño(enemigo) 
        enemigo._vida = enemigo._vida - daño 
        print(self._nombre, "ha realizado", daño, "puntos de daño a", enemigo._nombre) 
        if enemigo.esta_vivo(): 
          print("La vida de", enemigo._nombre, "es", enemigo._vida)
        else: 
            enemigo.morir()


    def get_fuerza(self): 
        return self._fuerza 
    def set_fuerza(self, fuerza): 
        self._fuerza += fuerza    
        if fuerza <= 0: 
            print ("Error, has introducido un valor negativo") 
        else:
            self._fuerza = fuerza 

# Herencia: es una tecnica de programacion orientada a objetos que consiste en crear una nueva clase a partir de una clase existente, heredando sus atributos y metodos, y agregando nuevos atributos y metodos propios.
class Guerrero(Personaje):  # la clase Guerrero hereda de la clase Personaje, lo que significa que el Guerrero tiene todos los atributos y metodos de la clase Personaje, ademas de sus propios atributos y metodos.
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) # se llama al constructor de la clase padre (Personaje) utilizando super() para inicializar los atributos heredados (nombre, fuerza, inteligencia, defensa, vida) con los valores recibidos como argumentos.
        self._espada = espada

    def cambiar_arma(self): # este metodo se encarga de cambiar el arma del guerrero, para eso se le pide al usuario que elija un arma entre dos opciones, y dependiendo de la opcion elegida, se asigna un nuevo valor a la espada del guerrero.
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 9: "))
        if opcion == 1:
            self._espada = 8
        elif opcion == 2:
            self._espada = 9
        else:
            print("Número de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("Espada: ", self._espada)

    def daño(self, enemigo):
        return self._fuerza*self._espada - enemigo._defensa

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._libro= libro

    def atributos(self):
        super().atributos()
        print("Libro", self._libro)

    def daño(self, enemigo):
        return self._inteligencia*self._libro - enemigo._defensa

class Pistolero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, revolver ):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida )
        self._revolver = revolver
    
    def atributos(self):
        super().atributos()
        print("Revolver", self._revolver)

    def daño(self,enemigo):
        return self._inteligencia*self._revolver - enemigo._defensa


Tama = Personaje("Tama", 20, 15, 10, 100,)
guts = Guerrero("Guts", 20 ,10, 10, 100, 5)
vanessa = Mago("vanessa", 20, 15, 10, 100, 5)
pepe = Pistolero("pepe", 20, 14, 10, 100, 6)
Tama.atributos()
guts.atributos()
vanessa.atributos()
pepe.atributos()
