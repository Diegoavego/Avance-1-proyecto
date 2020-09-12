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


def calorias(a,b):
    return (a*b)

if (goal==("subir")):
    print ("Calorias necesarias para subir")
    IMC=(peso/(altura**2))
    print ("Tu IMC es:", IMC)
    if (edad>17):
        if (paquete=="Muy Activo"):
            print (calorias(peso,45)+700)
           
        elif (paquete=="Activo"):
            print (calorias(peso,45)+500)
            
        elif (paquete=="Moderado"):
            print(calorias(peso,45)+250)
            
        elif (paquete=="Pasivo"):
            print(calorias(peso,45)+100)
            
    elif (edad<18):
            if (paquete=="Muy Activo"):
                print(calorias(peso,40)+450)
            elif (paquete=="Activo"):
                print(calorias(peso,40)+300)
                
            elif (paquete=="Moderado"):
                print(calorias(peso,40)+100)
               
            elif (paquete=="Pasivo"):
                print(calorias(peso,40)+75)
                
     
elif (goal==("mantener")):
    print ("Calorias necesarias para mantener")
    IMC=math.sqrt(peso/(altura**2))
    print (IMC)
    if (edad>17):
        if (paquete=="Muy Activo"):
            print (calorias(peso,40))
           
        elif (paquete=="Activo"):
            print (calorias(peso,35))
            
        elif (paquete=="Moderado"):
            print(calorias(peso,35))
            
        elif (paquete=="Pasivo"):
            print(calorias(peso,33))
            
    elif (edad<18):
            if (paquete=="Muy Activo"):
                print(calorias(peso,40))
            elif (paquete=="Activo"):
                print(calorias(peso,40))
                
            elif (paquete=="Moderado"):
                print(calorias(peso,35))
               
            elif (paquete=="Pasivo"):
                print(calorias(peso,30))
    
    
    
elif (goal==("bajar")):
    print("Calorias necesarias para bajar")
    IMC=math.sqrt(peso/(altura**2))
    print ("Tu IMC es:",IMC)
else:
    print ("Dato no valido")




    
