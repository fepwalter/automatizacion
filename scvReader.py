import csv as csv


# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 

with open('prueba.csv', newline='') as File:  
    reader = csv.reader(File, delimiter=';')
    for row in reader:
    	num_unico = row[0]
    	novedad = row[1]
    	if novedad == '22':
    		print("entregado")
    	elif novedad.lower() == 'rae':
    		print("Se retiro")
    	elif novedad.lower() == 'not':
    		print("notificacion")
    	elif novedad.lower() == 'ua':
    		print("unico aviso")
    		
del num_unico, novedad, reader  # Borrar objetos
File.close()  # Cerrar archivo
del File  
