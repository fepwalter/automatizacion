import pyautogui as robot
import time
import csv
from tkinter import messagebox


pos_aplicacion = 57,500
pos_anoOperativo = 1046,355
pos_numero_unico = 955,392
pos_novedad = 937,490
pos_cargar = 1129,392
pos_asignar = 907,695
archivo_csv = "robot.csv"

def moverMouse(pos,click=1):
	robot.moveTo(pos)
	robot.click(clicks=click)

def entrarAplicativoAsignarNovedad():
	moverMouse(pos_aplicacion, 2)
	robot.sleep(1)
	robot.hotkey("down")
	robot.hotkey("tab")
	robot.hotkey("enter")
	robot.sleep(2)
	robot.hotkey("alt")
	robot.typewrite("a")
	robot.hotkey("right")
	robot.hotkey("enter")
	robot.sleep(1)

def tipearNovedad(tecla, veces):
	for x in range(veces):
		robot.typewrite(tecla)
	robot.sleep(1)

def intro():
	robot.hotkey("enter")
	robot.sleep(1)

def cargar():
	moverMouse(pos_cargar)

def asignar():
	moverMouse(pos_asignar)
	robot.hotkey("enter")

def anoOperativo2021():
	robot.hotkey("up")
	robot.hotkey("enter")
	robot.sleep(1)

# leer csv, obtener campos del archivo
# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 

entrarAplicativoAsignarNovedad() # entramos al aplicativo a asignar novedad
with open(archivo_csv, newline='') as File:  
    reader = csv.reader(File, delimiter=';')
    for row in reader:
    	num_unico = row[0]
    	novedad = row[1]
    	moverMouse(pos_numero_unico) # meter numero unico
    	robot.typewrite(num_unico)
    	robot.sleep(1)
    	moverMouse(pos_novedad) # Posisionar en novedad
    	if novedad == '22':
    		tipearNovedad("2", 3)
    	elif novedad.lower() == 'rae':
    		tipearNovedad("r", 1)
    	elif novedad.lower() == 'not':
    		tipearNovedad("n", 2)
    	elif novedad.lower() == 'ua':
    		tipearNovedad("u", 1)
    	intro()
    	cargar()
    	asignar()
File.close()
with open(archivo_csv, newline='') as File:  
    reader = csv.reader(File, delimiter=';')
    #Paso a leer la columna 3 cono las novedades del 2021.
    moverMouse(pos_anoOperativo)
    anoOperativo2021()
    for row in reader:
    	num_unico = row[0]
    	novedad = row[2]
    	moverMouse(pos_numero_unico) # meter numero unico
    	robot.typewrite(num_unico)
    	robot.sleep(1)
    	moverMouse(pos_novedad) # Posisionar en novedad
    	if novedad == '22':
    		tipearNovedad("2", 3)
    	elif novedad.lower() == 'rae':
    		tipearNovedad("r", 1)
    	elif novedad.lower() == 'not':
    		tipearNovedad("n", 2)
    	elif novedad.lower() == 'ua':
    		tipearNovedad("u", 1)
    	intro()
    	cargar()
    	asignar()

del num_unico, novedad, reader  # Borrar objetos
File.close()  # Cerrar archivo
del File

messagebox.showinfo(message="Terminé craa", title="Happy Hour")