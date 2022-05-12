"""
Nivell 1
Exercici 1
L'exercici consisteix a crear un programa que et classifiqui una variable numèrica en funció de l’escala Suspès/Aprovat/Notable/Excel·lent.
"""

from sre_constants import _NamedIntConstant


nota1 = input("Introduce una nota: ")
nota= int(nota1)

if nota<5 :
    print ("Suspenso")
elif nota >=5 and nota<= 6 :
    print("Aprobado")
elif nota>=6 and nota< 7:
    print("Bien")
elif nota>= 7 and nota <9:
    print ("Notable")
else :
    print ("Sobresaliente")

print("***************************************")
"""
Exercici 2
Utilitzant el següent tutorial Programiz: Python Input, Output and Import crea un programa que et pregunti dos números.
T’ha de mostrar un missatge dient si el primer és més gran, el segon és més gran o són iguals.
"""
numero1 = input("Introduce el número 1: ")
numero1 = int(numero1)
numero2= input("Introduce el número 2: ")
numero2=int(numero2)

if numero1==numero2:
    print ("Los número son iguales")
elif numero1>numero2:
    print("El número ", numero1," es más grande que el número ",numero2)
else:
    print("El número " , numero2, " es mayor que el número ",numero1)

print("***************************************")
"""
Exercici 3
Crea un programa que et pregunti el teu nom, i et demani un número.
Si el número és 0, hauria de mostrar un missatge d’error.
En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número. Per exemple, “Joan Joan Joan”.
"""
nombre = input("Introcuce tu nombre: ")
numero = input("Introduce un número: ")
numero = int(numero)


if numero == 0:
    print("El número no es válido")
else:
    for i in range(numero):
       print (nombre, end=" ")

print("")
print("***************************************")


"""
Exercici 4
Crea un programa que donada una llista qualsevol, et digui si es simètrica o no. Si ho és, que et digui quants elements té.
"""

#miLista1 =[1,2,3,4,3,2,1] 
miLista1 = [25,15,48,15,25]

if miLista1[::] == miLista1[::-1]:
    print ("la lista es simétrica, y tiene ", len(miLista1), " elementos")
else: 
    print("la lista no es simétrica")

print("***************************************")

"""
Exercici 5
Crea un programa que donada una llista, et digui quants números coincideixen amb la seva posició.
Per exemple [3,4,2,0,2,3,6] el 2 i el 6 coincideixen.
"""
miLista =[3,4,2,0,2,3,6]
coinciden = []
for i in range (len(miLista)):
    if miLista[i]==i:
        coinciden.append(i)

print ("Los números que coinciden con su posición son: ", coinciden)    