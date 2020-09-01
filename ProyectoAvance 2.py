#CALORIESAVER
import math
altura=float(input("Indica tu altura en metros"))
peso=float(input("Indica tu peso en kilogramos"))
edad=int(input("Indica tu edad"))

act=int(input("¿Que tan activo eres durante el día?, 1:Muy Poco, 2:Poco, 3:Medianamente activo, 4:Activo, 5:Muy Activo"))

if (act <= 2):
    paquete=("Pasivo")
elif (act>5):
    print("Dato no existente")
elif (act==3):
    paquete=("Moderado")
elif (act==4):
    paquete=("Activo")
elif (act==5):
    paquete=("Muy Activo")
else:
    print("Dato no existente")


print ("Eres", paquete, "Deseas subir, bajar, o mantener peso?")

goal=str(input("usar minusculas porfavor"))

if (goal==("subir")):
    print ("Calorias necesarias para subir")
    IMC=(peso/(altura**2))
    print ("Tu IMC es:", IMC)
    if (edad>17):
        if (paquete=="Muy Activo"):
            Calorias=(peso*40)+700
            print (Calorias)
        elif (paquete=="Activo"):
            Calorias=(peso*40)+500
            print (Calorias)
        elif (paquete=="Moderado"):
            Calorias=(peso*40)+250
            print (Calorias)
        elif (paquete=="Pasivo"):
            Calorias=(peso*40)+100
            print(Calorias)
    elif (edad<18):
            if (paquete=="Muy Activo"):
                Calorias=(peso*40)+450
                print(Calorias)
            elif (paquete=="Activo"):
                Calorias=(peso*40)+300
                print (Calorias)
            elif (paquete=="Moderado"):
                Calorias=(peso*40)+100
                print (Calorias)
            elif (paquete=="Pasivo"):
                Calorias=(peso*40)+50
                print(Calorias)
     
elif (goal==("mantener")):
    print ("Calorias necesarias para mantener")
    IMC=math.sqrt(peso/(altura**2))
    print (IMC)
elif (goal==("bajar")):
    print("Calorias necesarias para bajar")
    IMC=math.sqrt(peso/(altura**2))
    print ("Tu IMC es:",IMC)
else:
    print ("Dato no valido")




    
#Falta mostrar si tu imc esta en el rango correcto, tu peso, etc.
#Despues te va a imprimir 3 opciones a tu agrado si deseas bajar subir o mantener peso
#y depende de la que selecciones te va a indicar las calorias 