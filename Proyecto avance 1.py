#CALORIESAVER

altura=int(input("Indica tu altura en centímetros"))
peso=float(input("Indica tu peso en kilogramos"))
edad=int(input("Indica tu edad"))

act=int(input("¿Que tan activo eres durante el día?, 1:Muy Poco, 2:Poco, 3:Medianamente activo, 4:Activo, 5:Muy Activo"))

if (act <= 2):
    print ("Paquete 1")
    
else:
    print("Paquete 2")
    
#A partir de aquí va a comenzar los calculas que agarran las variables y calcular calorias
#Despues te va a imprimir 3 opciones a tu agrado si deseas bajar subir o mantener peso
#y depende de la que selecciones te va a indicar las calorias 