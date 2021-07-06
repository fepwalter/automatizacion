import csv as csv
import os
import codigos_internos as ci

#obtener la direccion de los archivos
dir_entrada = os.getcwd()+"\\entrada\\"
dir_salida = os.getcwd()+"\\salida\\"

def cargarNovedad(cu,nov2020,nov2021,aCargar,obs):
	if aCargar.lower() == ci.COD_NINGUNO:
		return
	elif aCargar.lower() == ci.COD_AMBOS:
		writer.writerow([cu]+[nov2020]+[nov2021]+[obs])
	elif aCargar.lower() == ci.COD_2020:
		writer.writerow([cu]+[nov2020]+["null"]+[obs])
	elif aCargar.lower() == ci.COD_2021:	
		writer.writerow([cu]+["null"]+[nov2021]+[obs])
	#print(aCargar)
	
#for i, csv_file in enumerate (os.listdir(dir_entrada)): este sirve si queres crear archivos de salida distintos
#with open(dir_salida+"nombre"+str(i)+".csv","w",newline='') as csvFile:
for csv_file in os.listdir(dir_entrada):
	with open(dir_salida+"archivodecarga"+".csv","a",newline ='') as csvFile:
		writer = csv.writer(csvFile, delimiter=';')
		with open(dir_entrada+csv_file, newline='', encoding="ANSI") as File:
			reader = csv.reader(File, delimiter=';')
			for row in reader:
				if not row[40]:
					row[40]= ci.COD_NO_OBS
				cargarNovedad(row[1],row[37],row[38],row[39],row[40])
				#solo controla por fila (si solo hay que cambiar novedad de algun año no lo comprueba eso)
				#if row[39].lower() == "1": 
					#writer.writerow([row[1]]+[row[37]]+[row[38]]+[row[40]]) #+ para agregar celdas al lado

File.close()  # Cerrar archivo
del File  
