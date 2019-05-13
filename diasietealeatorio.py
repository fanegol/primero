#importamos la libreria randint
from random import randint
aleatorio=randint(0,20) #creamos una variable
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio) #imprimimos el numero generado
#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes, y elegir a uno de los participantes
#aleatoriamente y retornar esa persona elegida
#desafio: no volver a retornar una persona ya sorteada
    
from random import randint #importamos la funcion randint de la libreria 

def sorteo(lista1):    #definimos la funcion 
    aleatorio=randint(0,len(lista1)-1) #llamamos la funcion randint()
    ganador=lista1[aleatorio]
    return ganador

listasorteo=["Francisco","Maria","Mauricio","Margaret"]
resultado=sorteo(listasorteo)
print(resultado)

