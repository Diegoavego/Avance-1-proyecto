#CALORIESAVER
"""Este programa te indica tu IMC y segun tus objetivos te recomienda la cantidad de calorias
que deberías comer al día aproximadamente."""

"""Bibliotecas"""
#Usamos la biblioteca de math para usar operaciones matematicas como cuadrados
import math   

#Usamos tabulate para poder imprimir las listas en forma de tabla y que se vea ordenado y limpio
from tabulate import tabulate 

"================================================================="


"""El programa recibe el nombre y apellido del usuario"""


n=str(input("Escribe tu nombre: "))
p=str(input("Escribe tu apellido: "))


                      
                      
"====================FUNCIONES========================================="
"""(Uso de funciones Y Parametros)
Definimos el nombre y apellido de las variables del usuario
y se imprimen en formato de nombre y apellido. Regresa estos datos
para llamar a la funcion y que los datos se queden guardados"""

def usuario(nombre="",apellido=""):
    print("Hola",nombre,apellido)
    print ("A continuación tomaremos tus datos...")
    return usuario


"""(Uso de funciones, condicionales y ciclos)
Definimos cual es la actividad del usuario durante el día y dependiendo de su respuesta
determinamos las variables más adelante. Recibe un entero del usuario y no permite que se
introduzca un numero erroneo que no este dentro de las opciones, si el usuario lo hace
regresa a la pregunta. Devuelve el numero que introduce el usuario"""


def act ():
    while True:
        act=int(input("""¿Que tan activo eres durante el día?
                      1:Muy Poco
                      2:Poco
                      3:Medianamente activo
                      4:Activo
                      5:Muy Activo"""))
    
        if 1<=act<=5:
            break
        
        else:
            print ("Debes seleccionar una opcion (1, 2, 3, 4 o 5)")
    return act
        

"""(Uso de funciones, condicionales y operadores)
Definimos a que paquete pertence el usuario segun que tan activo es durante el día para usarlo
en el programa central, si es pasivo, moderado o activo. Regresa la variable paquete como string"""

def paquete_funcion():
    if (actividad==1) or (actividad==2):
        paquete=("Pasivo")
        
    elif actividad==3:
        paquete=("Moderado")
        
    elif actividad==4:
        paquete=("Activo")
        
    elif actividad==5:
        paquete=("Muy Activo")
    return paquete
    
    
    
    

"""(Uso de funciones, operaciones y parametros)
Definimos la operación para el programa central para sacar las calorias.
Multiplica los parametros y devuelve el producto"""
def calorias(a,b):
    return (a*b)


"""(Funciones)
Se define la operacion para sacar el IMC del usuario. Se toma
de la lista de los datos del usuario su peso y este se divide entre
su altura al cuadrado. Se imprime el resultado de IMC limitando a 2 decimales
y se devuelve el valor"""

def IMC_usuario ():
    IMC=(datos[0]/(datos[1]**2))
    print ("Tu IMC es:","{:.2f}".format(IMC),"%")
    
    return IMC


"""(Funciones)
Definimos el objetivo del usuario, si desea bajar, mantener o subir de peso.
Recibe un string del usuario y lo guarda en la variable. Devuelve la variable, goal"""

def goal_funcion ():
    print ("Deseas subir, bajar, o mantener peso?")
    goal=str(input("Usar minusculas porfavor: "))
    return goal
"==========================================================================================="

#Mandamos a llamar la funcion usuario
usuario(n,p)



"""(Uso de listas)
Guardamos en la lista el peso, altura y edad del usuario para que sea facil acceder a ellas y
mas adelante las podamos tabular"""

datos=[float(input("Indica tu peso: ")),
       (float(input("Indica tu altura en metros: "))),
       (int(input("Indica tu edad: ")))
       ]


#Mandamos a llamar act asignando el valor a una variable que vamos a necesitar en la siguiente funcion

actividad=act()


#Mandamos a llamar paquete y lo guardamos en la variable paquete

paquete=paquete_funcion()


#Mandamos a llamar el objetivo del usuario y lo guardamos en goal

goal=goal_funcion()
    
#Mandamos a llamar el imc del usuario y lo guardamos en la variable imc

imc=IMC_usuario()



"=======================Programa=Central====================================="
"""(Condicionales anidadas y uso de los datos de la lista)"""
#Rescata todos los datos guardados anteriormente y comienza a calcular las calorias


if (goal==("subir")) and (datos[2]>17):
    
    
    print ("Calorias necesarias para subir:")
    
    
    if (paquete=="Muy Activo"):
            print (calorias(datos[0],45)+1200)
           
    elif (paquete=="Activo"):
            print (calorias(datos[0],45)+1000)
            
    elif (paquete=="Moderado"):
            print(calorias(datos[0],45)+800)
            
    elif (paquete=="Pasivo"):
            print(calorias(datos[0],45)+500)
            
elif (goal==("subir")) and (datos[2]<18):
    
    
    print ("Calorias necesarias para subir:")
    if (paquete=="Muy Activo"):
                print(calorias(datos[0],40)+1100)
    elif (paquete=="Activo"):
                print(calorias(datos[0],40)+900)
                
    elif (paquete=="Moderado"):
                print(calorias(datos[0],40)+700)
               
    elif (paquete=="Pasivo"):
                print(calorias(datos[0],40)+500)
                


elif (goal==("mantener")) and (datos[2]>17):
    
    
    print ("Calorias necesarias para mantener:")
    
    if (paquete=="Muy Activo"):
            print (calorias(datos[0],45)+200)
           
    elif (paquete=="Activo"):
            print (calorias(datos[0],45)+150)
            
    elif (paquete=="Moderado"):
            print(calorias(datos[0],45))
            
    elif (paquete=="Pasivo"):
            print(calorias(datos[0],45))
            
elif (goal==("mantener")) and (datos[2]<18):
    
    
    print ("Calorias necesarias para mantener:")
    
    if (paquete=="Muy Activo"):
                print(calorias(datos[0],40)+150)
    elif (paquete=="Activo"):
                print(calorias(datos[0],40)+100)
                
    elif (paquete=="Moderado"):
                print(calorias(datos[0],40))
               
    elif (paquete=="Pasivo"):
                print(calorias(datos[0],40))
    
  
    
elif (goal==("bajar")) and (datos[2]>17):
    
    
    print("Calorias necesarias para bajar:")
    
    if (paquete=="Muy Activo"):
            print (calorias(datos[0],45)-900)
           
    elif (paquete=="Activo"):
            print (calorias(datos[0],45)-1000)
            
    elif (paquete=="Moderado"):
            print(calorias(datos[0],45)-1100)
            
    elif (paquete=="Pasivo"):
            print(calorias(datos[0],45)-1300)
            
elif (goal==("bajar")) and (datos[2]<18):
    
    
    print ("Calorias necesarias para bajar:")
    
    if (paquete=="Muy Activo"):
                print(calorias(datos[0],40)-150)
    elif (paquete=="Activo"):
                print(calorias(datos[0],40)-250)
                
    elif (paquete=="Moderado"):
                print(calorias(datos[0],40)-350)
               
    elif (paquete=="Pasivo"):
                print(calorias(datos[0],40)-400)
                
    
else:
    print ("Dato no valido")


#Resultados
print("A continuación te mostramos la tabla de IMC:")


"""(uso de listas y biblioteca importada)"""

tabla_imc=[["Hasta 15.99",     "Extremadamente Delagado"],
           ["De 16 a 18.49",   "Delgado"],
           ["De 18.50 a 24.99","Peso adecuado"],
           ["De 25 a 29.99",   "Sobrepeso"],
           ["30 o más",        "obesidad"]
           ]

print(tabulate(tabla_imc))


#Posicion en la tabla de IMC
"""Usamos la biblioteca de tabulate para que la lista se imprima en formato de tabla y sea
mas visual para el usuario"""

print("Estas en:")

"""(Condicionales, Uso de listas)
Recuperamos el valor de la funcion imc y la
ponemos en esta condicional que determina segun los
datos del usuario su lugar en la tabla anterior de IMC"""

if imc<15.99:
        print(tabla_imc[0][1])
elif 16<imc<18.49:
        print(tabla_imc[1][1])
elif 18.50<imc<24.99:
        print(tabla_imc[2][1])
elif 25<imc<29.99:
        print(tabla_imc[3][1])
else:
        print(tabla_imc[4][1])



              


    
