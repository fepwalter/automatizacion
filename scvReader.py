import csv as csv


# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 
with open("pruba1.csv","w",newline ='') as csvFile:
	writer = csv.writer(csvFile, delimiter=',', quoting = 'quote_minimal')
	with open('Hoja de Ruta Deborah Salida3 - Hoja 1.csv', newline='', encoding="utf-8") as File:  
		reader = csv.reader(File, delimiter=',')
		for row in reader:
			#entrada = row[1]
			writer.writerow(row[1])
			

File.close()  # Cerrar archivo
del File  
