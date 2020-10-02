#CALORIESAVER
import math

#Lista para los datos que introduce el usuario
Datos=[float(input("Indica tu peso:")),
       (float(input("Indica tu altura en metros:"))),
       (int(input("Indica tu edad:")))]

while True:
    act=int(input("""¿Que tan activo eres durante el día?
    1:Muy Poco
    2:Poco
    3:Medianamente activo
    4:Activo
    5:Muy Activo"""))
    
    if act==1:
        paquete=("Pasivo")
        break
    elif act==2:
        paquete=("Pasivo")
        break
    elif act==3:
        paquete=("Moderado")
        break
    elif act==4:
        paquete=("Activo")
        break
    elif act==5:
        paquete=("Muy Activo")
        break
    else:
        print ("Debes seleccionar una opcion (1, 2, 3, 4 o 5)")

print ("Eres", paquete, "Deseas subir, bajar, o mantener peso?")
goal=str(input("usar minusculas porfavor"))
    


def calorias(a,b):
    return (a*b)

if (goal==("subir")):
    print ("Calorias necesarias para subir")
    IMC=(Datos[0]/(Datos[1]**2))
    print ("Tu IMC es:",IMC,"%")
    if (Datos[2]>17):
        if (paquete=="Muy Activo"):
            print (calorias(Datos[0],45)+1700)
           
        elif (paquete=="Activo"):
            print (calorias(Datos[0],45)+1200)
            
        elif (paquete=="Moderado"):
            print(calorias(Datos[0],45)+900)
            
        elif (paquete=="Pasivo"):
            print(calorias(Datos[0],45)+500)
            
    elif (Datos[2]<18):
            if (paquete=="Muy Activo"):
                print(calorias(Datos[0],40)+1100)
            elif (paquete=="Activo"):
                print(calorias(Datos[0],40)+900)
                
            elif (paquete=="Moderado"):
                print(calorias(Datos[0],40)+700)
               
            elif (paquete=="Pasivo"):
                print(calorias(Datos[0],40)+500)
                
     
elif (goal==("mantener")):
    print ("Calorias necesarias para mantener")
    IMC=(Datos[0]/(Datos[1]**2))
    print ("Tu IMC es:", IMC,"%")
    if (Datos[2]>17):
        if (paquete=="Muy Activo"):
            print (calorias(Datos[0],40))
           
        elif (paquete=="Activo"):
            print (calorias(Datos[0],35))
            
        elif (paquete=="Moderado"):
            print(calorias(Datos[0],35))
            
        elif (paquete=="Pasivo"):
            print(calorias(Datos[0],33))
            
    elif (Datos[2]<18):
            if (paquete=="Muy Activo"):
                print(calorias(Datos[0],40))
            elif (paquete=="Activo"):
                print(calorias(Datos[0],40))
                
            elif (paquete=="Moderado"):
                print(calorias(Datos[0],35))
               
            elif (paquete=="Pasivo"):
                print(calorias(Datos[0],30))
    
    
    
elif (goal==("bajar")):
    print("Calorias necesarias para bajar")
    IMC=(Datos[0]/(Datos[1]**2))
    print ("Tu IMC es:",IMC,"%")
    
     if (Datos[2]>17):
        if (paquete=="Muy Activo"):
            print (calorias(Datos[0],45)-1700)
           
        elif (paquete=="Activo"):
            print (calorias(Datos[0],45)-1200)
            
        elif (paquete=="Moderado"):
            print(calorias(Datos[0],45)+900)
            
        elif (paquete=="Pasivo"):
            print(calorias(Datos[0],45)+500)
            
    elif (Datos[2]<18):
            if (paquete=="Muy Activo"):
                print(calorias(Datos[0],40)+1100)
            elif (paquete=="Activo"):
                print(calorias(Datos[0],40)+900)
                
            elif (paquete=="Moderado"):
                print(calorias(Datos[0],40)+700)
               
            elif (paquete=="Pasivo"):
                print(calorias(Datos[0],40)+500)
                
    
else:
    print ("Dato no valido")




    
