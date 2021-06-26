import csv as csv


# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 
with open("pruba1.csv","w",newline ='') as csvFile:
	writer = csv.writer(csvFile, delimiter=',')
	with open('Hoja de Ruta Deborah Salida3 - Hoja 1.csv', newline='', encoding="utf-8") as File:  
		reader = csv.reader(File, delimiter=',')
		for row in reader:
			try:
				#entrada = row[1]
				writer.writerow([row[1],row[37],row[38]])
			except:
				print("vacio")


File.close()  # Cerrar archivo
del File  
