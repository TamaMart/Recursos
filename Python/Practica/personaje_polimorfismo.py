class Personaje:

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self._nombre = nombre  
        self._fuerza = fuerza  
        self._inteligencia = inteligencia
        self._defensa = defensa 
        self._vida = vida 


    def atributos(self): 
        print(self._nombre, ":", sep="") # el nombre del personaje se imprime seguido de dos puntos, sin espacio entre ellos (sep="")
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


class Guerrero(Personaje):  
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) 
        self._espada = espada

    def cambiar_arma(self):
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

# Polimorfismo: es una tecnica de programacion orientada a objetos que consiste en la capacidad de un objeto de tomar muchas formas, es decir, un objeto puede ser tratado como un objeto de su clase padre o como un objeto de su propia clase. En este ejemplo, el metodo daño es un metodo polimorfico, ya que cada clase hija (Guerrero, Mago, Pistolero) tiene su propia implementacion del metodo daño, lo que significa que el mismo metodo puede tener diferentes comportamientos dependiendo del tipo de objeto que lo llame.
def combate(guts, vanessa):  # este metodo se encarga de simular un combate entre dos personajes, en este caso entre guts y vanessa. El combate se realiza en turnos, donde cada personaje ataca al otro en cada turno hasta que uno de los personajes muere. El metodo recibe como argumentos los dos personajes que van a combatir.
        turno =0
        while guts.esta_vivo() and vanessa.esta_vivo(): # se verifica si ambos personajes estan vivos utilizando el metodo esta_vivo de cada personaje, si ambos personajes estan vivos, se realiza un turno de combate.
            print("\nturno", turno)
            print(">>> accion de", vanessa._nombre, ":", sep=" ")
            vanessa.atacar(guts)
            print(">>> accion de", guts._nombre, ":", sep=" ")
            guts.atacar(vanessa)
            turno=turno + 1
        if vanessa.esta_vivo(): # se verifica si vanessa esta viva utilizando el metodo esta_vivo de vanessa, si es asi, se imprime un mensaje indicando que ha ganado vanessa. 
            print("\nHa ganado", vanessa._nombre)  
        elif guts.esta_vivo(): 
            print("\nHa ganado", guts._nombre)   
        else:
            print("\nEmpate")   


guts.cambiar_arma() # se llama al metodo cambiar_arma del personaje guts para cambiar su arma antes de iniciar el combate.
combate(vanessa, guts)



Tama.atributos()
guts.atributos()
vanessa.atributos()
pepe.atributos()
