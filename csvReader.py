import csv as csv


# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 
with open("prueba1.csv","w",newline ='') as csvFile:
	writer = csv.writer(csvFile, delimiter=';')
	with open('Hoja de Ruta Deborah Salida3.csv', newline='', encoding="ANSI") as File:
		reader = csv.reader(File, delimiter=';')
		for row in reader:
			writer.writerow([row[1]]+[row[37]]+[row[38]]) #+ para agregar celdas al lado

File.close()  # Cerrar archivo
del File  
