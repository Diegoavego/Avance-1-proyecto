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
    
    if 1<act<5:
        if act==1:
            paquete=("Pasivo")
        
        elif act==2:
            paquete=("Pasivo")
        
        elif act==3:
            paquete=("Moderado")
        
        elif act==4:
            paquete=("Activo")
        
        elif act==5:
            paquete=("Muy Activo")
        break
        
    else:
        print ("Debes seleccionar una opcion (1, 2, 3, 4 o 5)")
        
      

print ("Eres", paquete, "Deseas subir, bajar, o mantener peso?")
goal=str(input("usar minusculas porfavor"))
    


def calorias(a,b):
    return (a*b)

if (goal==("subir")) and (Datos[2]>17):
    IMC=(Datos[0]/(Datos[1]**2))
    print ("Tu IMC es:","{:.2f}".format(IMC),"%")
    print ("Calorias necesarias para subir:")
    
    
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
                
     
elif (goal==("mantener")) and (Datos[2]>17):
    IMC=(Datos[0]/(Datos[1]**2))
    print ("Tu IMC es:","{:.2f}".format(IMC),"%")
    print ("Calorias necesarias para mantener:")
    
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
    
    
    
elif (goal==("bajar")) and (Datos[2]>17):
    IMC=(Datos[0]/(Datos[1]**2))
    print ("Tu IMC es:","{:.2f}".format(IMC),"%")
    print("Calorias necesarias para bajar:")
    
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



tabla_imc=["Hasta 15.99", "Extremadamente Delagado"],["De 16 a 18.49", "Delgado"],["De 18.50 a 24.99","Peso adecuado"],["De 25 a 29.99","Sobrepeso"],["30 o más", "obesidad"]

print((tabla_imc))

print("Estas en:")

if IMC<15.99:
        print(tabla_imc[0][1])
elif 16<IMC<18.49:
        print(tabla_imc[1][1])
elif 18.50<IMC<24.99:
        print(tabla_imc[2][1])
elif 25<IMC<29.99:
        print(tabla_imc[3][1])
else:
        print(tabla_imc[4][1])
        

              


    
