import pyautogui as robot
import time
import csv
from tkinter import messagebox
import os
import codigos_internos as ci

dir_salida = os.getcwd()+"\\salida\\"
pos_aplicacion = 57,500
archivo_csv = dir_salida+"archivodecarga.csv"

#variables de posicion para el modulo de asignado de novedad
pos_anoOperativo = 1046,355
pos_numero_unico = 955,392
pos_novedad = 937,490
pos_cargar = 1129,392
pos_asignar = 907,695
pos_cuadro_observ = 950,550
pos_cerrar_asig = 1163,303

#variables de posicion para el modulo de Notificaciones
pos_cargar_unico = 870,453
pos_contacto = 830,517
pos_numero_not = 830,551
pos_cerrar_nots = 1280,371
pos_operativo_not = 1006,414

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

def posicionarOperativo2021():
	moverMouse(pos_anoOperativo)
	robot.hotkey("up")
	robot.hotkey("enter")
	robot.sleep(1)

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
				elif novedad.lower() == 'rae':
					tipearNovedad("r", 1, num_unico)
				elif novedad.lower() == 'not':
					contador +=1
					tipearNovedad("n", 2, num_unico)
				elif novedad.lower() == 'ua':
					tipearNovedad("u", 1, num_unico)
				elif novedad.lower() == 'c':
					tipearNovedad('c', 1, num_unico)
				elif novedad.lower() == 'cfa':
					tipearNovedad('c', 7, num_unico)
				elif novedad.lower() == '26v':
					tipearNovedad("2",7, num_unico)
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
def main(): 
	entrarAplicativo()
	irAmenuAsignar()
	contadorNot2020 = lectura_carga_novedades(2020)
	posicionarOperativo2021()
	contadorNot2021 = lectura_carga_novedades(2021)
	moverMouse(pos_cerrar_asig)

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

if __name__=='__main__':
	main()
	messagebox.showinfo(message="Terminé craa", title="Tomando un feca")