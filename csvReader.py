import csv as csv
import os

#obtener la direccion de los archivos
dir_entrada = os.getcwd()+"\\entrada\\"
dir_salida = os.getcwd()+"\\salida\\"

#for i, csv_file in enumerate (os.listdir(dir_entrada)): este sirve si queres crear archivos de salida distintos
#with open(dir_salida+"nombre"+str(i)+".csv","w",newline='') as csvFile:
for csv_file in os.listdir(dir_entrada):
	with open(dir_salida+"archivodecarga"+".csv","a",newline ='') as csvFile:
		writer = csv.writer(csvFile, delimiter=';')
		with open(dir_entrada+csv_file, newline='', encoding="ANSI") as File:
			reader = csv.reader(File, delimiter=';')
			for row in reader:
				#solo controla por fila (si solo hay que cambiar novedad de algun año no lo comprueba eso)
				if row[39].lower() == "true": 
					writer.writerow([row[1]]+[row[37]]+[row[38]]) #+ para agregar celdas al lado

File.close()  # Cerrar archivo
del File  
