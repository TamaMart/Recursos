#Funciones 

var_altura = int(input("ingrese su altura: "))
def mostraraltura(altura):
    resultado=""
    if altura >= 175: 
        resultado = "Eres una persona alta"
        
    else:
        resultado = "Eres una persona baja"

    return resultado
 
print(mostraraltura(var_altura))  
