import pyautogui as robot
import time
import csv
from tkinter import *
import os
import codigos_internos as ci
import cod_PosicionesCasa as pc
#import cod_PosicionesOficina as po

dir_salida = os.getcwd()+"\\salida\\"
pos_aplicacion = 57,500
archivo_csv = dir_salida+"archivodecarga.csv"

def moverMouse(pos,click=1):
	robot.moveTo(pos)
	robot.click(clicks=click)

def irAmenu(hotkey,veces):
	robot.hotkey("alt")
	robot.typewrite("a")
	for i in range(veces):
		robot.hotkey(hotkey)

def irAmenuNots():
	irAmenu("down",4)
	robot.hotkey("right")
	robot.hotkey("enter")
	robot.hotkey("enter")
	robot.sleep(1)

def irAmenuAsignar():	
	irAmenu("right",1)
	robot.hotkey("enter")
	robot.sleep(1)

def entrarAplicativo():
	moverMouse(pos_aplicacion, 2)
	robot.sleep(1)
	robot.hotkey("down")
	robot.hotkey("tab")
	robot.hotkey("enter")
	robot.sleep(2)

def tipearNovedad(tecla, veces, num_unico):
	moverMouse(pos_numero_unico) # meter numero unico
	robot.typewrite(num_unico)
	robot.sleep(1)
	robot.hotkey("tab")#moverMouse(pos_novedad) # Posisionar en novedad
	for x in range(veces):
		robot.typewrite(tecla)
	robot.hotkey("tab")
	robot.sleep(1)

def intro():
	robot.hotkey("enter")
	robot.sleep(1)

def cargar():
	moverMouse(pos_cargar)
	robot.sleep(1)

def asignar():
	moverMouse(pos_asignar)
	robot.hotkey("enter")

def posicionarOperativo2020():
	moverMouse(pos_anoOperativo)
	robot.hotkey("down")
	robot.hotkey("enter")
	robot.sleep(1)

def cargar_posiciones(pos):
	#variables de posicion para el modulo de asignado de novedad
	pos_anoOperativo = pos.POS_ANIO_OPERATIVO_ASIG
	pos_numero_unico = pos.POS_NUMERO_UNICO
	pos_novedad = pos.POS_NOVEDAD
	pos_cargar = pos.POS_CARGAR
	pos_asignar = pos.POS_ASIGNAR
	pos_cuadro_observ = pos.POS_CUADRO_OBSERVACIONES
	pos_cerrar_asig = pos.POS_CERRAR_ASIGNACION

	#variables de posicion para el modulo de Notificaciones
	pos_cargar_unico = pos.POS_CARGAR_UNICO
	pos_contacto = pos.POS_CONTACTO
	pos_numero_not = pos.POS_NUMERO_NOT
	pos_cerrar_nots = pos.POS_ANIO_OPERATIVO_NOT
	pos_operativo_not = pos.POS_CERRAR_NOTIFICACIONES

def lectura_carga_novedades(anio):
	contador = 0
	with open(archivo_csv, newline='') as File:
		reader = csv.reader(File, delimiter=';')
		for row in reader:
			num_unico = row[0]
			obsvervacion = row[3]
			if anio == 2020:
				novedad = row[1]
			else:
				novedad = row[2]
			if novedad.lower() != 'null':
				if novedad == '22':
					tipearNovedad("2", 3, num_unico)
				elif novedad.lower() == ci.COD_RETIRADA:
					tipearNovedad("r", 1, num_unico)
				elif novedad.lower() == ci.COD_NOTIFICACION:
					contador +=1
					tipearNovedad("n", 2, num_unico)
				elif novedad.lower() == ci.COD_UNICO_AVISO:
					tipearNovedad("u", 1, num_unico)
				elif novedad.lower() == ci.COD_SIN_ACTIVIDAD:
					tipearNovedad("1", 6, num_unico)
				elif novedad.lower() == ci.COD_ASIGNADA_ENCUESTADOR:
					tipearNovedad("2", 2, num_unico)
				elif novedad.lower() == ci.COD_FUSION:
					tipearNovedad("1", 5, num_unico)
				elif novedad.lower() == ci.COD_CUMPLIMENTADO:
					tipearNovedad('c', 1, num_unico)
				elif novedad.lower() == ci.COD_FALTA_REVISAR:
					tipearNovedad('c', 7, num_unico)
				elif novedad.lower() == ci.COD_NO_UBICABLE_VIRTUAL:
					tipearNovedad("2",7, num_unico)
				elif novedad.lower() == ci.COD_PRORROGA:
					tipearNovedad('p', 1, num_unico)
				#comprobar si hay codigo 4(NO_OBS)
				if obsvervacion != ci.COD_NO_OBS:
					robot.typewrite(obsvervacion)
				#intro()
				cargar()
				asignar()
			else:
				print("no hago nada")
				
	File.close()
	return contador
	
def asignarNots(contador):
	for i in range(contador):
		moverMouse(pos_cargar_unico)
		#intro()solo para los casos en que ya haya una not previa
		moverMouse(pos_contacto)
		robot.typewrite("not")
		moverMouse(pos_numero_not)
		robot.typewrite(str(i))
		intro()
		intro()
	moverMouse(pos_cerrar_nots)
	robot.sleep(1)
	
# entramos al aplicativo a asignar novedad

#entrarAplicativo()
opcion = int(input("opcion 1 para cargar los valores de casa."))
if opcion == 1:
	cargar_posiciones(pc)
#else:
	#cargar_posiciones(po)

irAmenuAsignar()
contadorNot2021 = lectura_carga_novedades(2021)
posicionarOperativo2020()
contadorNot2020 = lectura_carga_novedades(2020)
moverMouse(pos_cerrar_asig)

#Modulo para el cargado de las NOT: se puede poner un flag para que no lo haga en caso que no se haya cargado ninduna not.
#contadorNot2020 = 
#contadorNot2021 = 
irAmenuNots()#entra al modulo de not ya en 2020
asignarNots(contadorNot2020)

#para entrar al modulo de not pero al 2021:	
irAmenuNots()
moverMouse(pos_operativo_not)
robot.hotkey("up")
robot.hotkey("enter")
asignarNots(contadorNot2021)

#generar los UA en PDF
irAmenu('down',3)
robot.hotkey('right')
robot.hotkey('down')
robot.hotkey('down')
robot.hotkey('down')
robot.hotkey('down')
robot.hotkey('enter')

messagebox.showinfo(message="Terminé craa", title="Tomando un feca")