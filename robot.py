import pyautogui as robot
import time
import csv

pos_numero_unico = 955,392
pos_novedad = 937,490
pos_cargar = 1129,392
pos_asignar = 907,695

def moverMouse(pos,click=1):
	robot.moveTo(pos)
	robot.click(clicks=click)

# leer csv, obtener campos del archivo
novedad = "RAE"
numero_unico = "06-002731-3"

# meter numero unico
moverMouse(pos_numero_unico)
robot.typewrite(numero_unico)
robot.sleep(1)

# Posisionar en novedad
moverMouse(pos_novedad)

# validar novedades
if novedad == "RAE":
	robot.typewrite("r")
	robot.sleep(1)

# meter novedad
robot.hotkey("enter")
robot.sleep(1)

# cargar
moverMouse(pos_cargar)

# asignar
moverMouse(pos_asignar)
robot.hotkey("enter")