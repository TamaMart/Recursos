class trabajador:
    def __init__(self, nombre, dinero, energia, trabajo):
        self.nombre = nombre
        self.__dinero = dinero
        self.energia = energia
        self.trabajo = trabajo

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Dinero:", self.__dinero)
        print("Energía:", self.energia)
        print("Trabajo:", self.trabajo)
    
    def trabajar (self):
        horas = int(input("¿Cuántas horas trabajó? "))
        self.__dinero += 2800 * horas
        self.energia -= 10 * horas
        print("has ganado",self.__dinero,"pesos")
        if self.energia <= 0: 
            self.energia = 0
            print("No tienes energía para trabajar, descansa un poco")
        else:
            print("te queda",self.energia,"de energía")

    def ganancias(self):
        productos_vendidos = int(input("¿Cuántos productos vendiste? "))
        self.__dinero += 1000 * productos_vendidos
        print("has ganado un total de",self.__dinero,"pesos en el dia de hoy")

    def descansar(self):
        horas_descanso = int(input("¿Cuántas horas vas a dormir? "))
        self.energia += 15 * horas_descanso
        if self.energia > 100:
            self.energia = 100
        if self.energia >= 100:
            print("te has recuperado, tu energía ahora es de",self.energia) 
        else:
              self.energia<100
              print ("duerme un poco más, tu energía actual es de: ",self.energia)

    def get_dinero (self):
        return self.__dinero

    def set_dinero (self, nuevo_dinero):
        if nuevo_dinero <=0:
           print ("Tu tienes que tlabajal")
        else: 
             self.__dinero = nuevo_dinero  


mi_trabajador = trabajador("Jorge", 100, 100, "agricultor")
mi_trabajador.set_dinero(50)
mi_trabajador.atributos()
mi_trabajador.trabajar()
mi_trabajador.ganancias()
mi_trabajador.descansar()

#instancia 2
mi_trabajador = trabajador("Simon", 100, 100, "pastelero")
mi_trabajador.set_dinero(500)
mi_trabajador.atributos()
mi_trabajador.trabajar()
mi_trabajador.ganancias()
mi_trabajador.descansar()

#instancia 3

mi_trabajador = trabajador("Maria", 100, 100, "empresaria")
mi_trabajador.set_dinero(5000)
mi_trabajador.atributos()
mi_trabajador.trabajar()
mi_trabajador.ganancias()
mi_trabajador.descansar()
