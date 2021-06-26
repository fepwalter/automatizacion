import csv as csv
import os

dir_entrada = os.getcwd()+"\\entrada\\"
dir_salida = os.getcwd()+"\\salida\\salida.csv"

for csv_file in os.listdir(dir_entrada):
	# Leer el archivo 'datos.csv' con reader() y 
	# realizar algunas operaciones básicas: 
	with open(dir_salida,"w",newline ='') as csvFile:
		writer = csv.writer(csvFile, delimiter=';')
		with open(dir_entrada+csv_file, newline='', encoding="ANSI") as File:
			reader = csv.reader(File, delimiter=',')
			for row in reader:
				writer.writerow([row[1]]+[row[37]]+[row[38]]) #+ para agregar celdas al lado

File.close()  # Cerrar archivo
del File  
