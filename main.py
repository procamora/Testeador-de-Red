import utils
import speedtest
import smtp
import funciones
import Compresion
import gui
import sys
import os
import glob
from changeip import listaAdaptadores, batSTATIC, batDHCP, runRoot


ruta = funciones.CreaDirectorioTrabajo()
image = './images/personal.gif'

#Test Completo
#SpeedTest, Utils,Comprimir, email
def Completo():
	funciones.LimpiaDirectorio(ruta)
	speedtest.main()
	utils.main()
	ProcesosComunes()


#Test de velocidad
#SpeedTest, Comprimir, email
def TestVelocidad():
	funciones.LimpiaDirectorio(ruta)
	speedtest.main()
	ProcesosComunes()


#Diagnostico
#Utils, Comprimir, email
def Diagnostico():
	funciones.LimpiaDirectorio(ruta)
	utils.main()
	ProcesosComunes()


def Comprime():
	fichero = Compresion.main()
	return fichero


def Email(adjuntos):
	smtp.main(adjuntos)
	gui.msgbox('Mensaje Enviado')


def MuestarResultados():
	'''Implementare en un futoro para que se vea bien visualmente'''
	#filename = os.path.normcase('%s\\speedtest.github'%(ruta))
	lista = glob.glob('%s\\*.github'%ruta)
	completo = ''
	for i in lista:
		f = open(i, 'r')
		text = f.read()
		completo += i.upper()
		completo += '\n'
		completo += text.replace('\r','\n')
		completo += '\n\n\n\n\n' 
		f.close()
	gui.textbox('Contents of file ', 'Show File Contents', completo)
	main()


def ProcesosComunes():
	fich = Comprime()
	msg = 'Enviar correo a github con tus resultados?'
	choices = ['Enviar','No Enviar y salir','Volver al menu']
	opciones = gui.buttonbox(msg, image=image, choices=choices)
	if opciones:
		if opciones == choices[0]:
			try:
				Email(fich)
			except:
				gui.msgbox('Hubo un problema al enviar el correo')
				main()
		elif opciones == choices[1]:
			print('no enviar')					#
			sys.exit(0)
		elif opciones == choices[2]:
			print('menu')
			main()
	else:
		print('no')
		sys.exit(0)


def Adaptadores():
	msg = "Selecciona el modo que quieres:"
	choices = ["DHCP","STATIC"]
	reply = gui.buttonbox(msg, choices=choices)
	if reply == None:
		sys.exit(0)
	msg = "Selecciona el adaptador que deseas modificar:"
	choiceAdap = listaAdaptadores()
	adaptador = gui.buttonbox(msg, choices=choiceAdap)
	if adaptador == None:
		sys.exit(0)

	if reply == choices[1]:
		print('static')
		dat = funciones.ipWMI()

		msg ="Introduce la nueva ip"
		title = "Utilidades de diagnostico"
		fieldNames  = ["ip", "subnet", "gateway", 'dnsServers1', 'dnsServers2']
		fieldValues = [dat["ip"], dat["subnet"], dat["gateway"], dat['dnsServers1'], dat['dnsServers2']]
		choice = gui.multenterbox(msg,title, fieldNames, fieldValues)
		if choice == None:
			sys.exit(0)
		batSTATIC(adaptador, choice)
		
	elif reply == choices[0]:
		print('dhcp')
		batDHCP(adaptador)
	
	
def EnProceso():
	gui.msgbox('Funcionalidad en proceso')
	main()

def nada():
	print('nada')

def main():
	msg ='Que prueba quieres realizar'
	title = 'Utilidades de diagnostico'
	choices = ['1. Diagnostico Completo (Test de velocidad, ping, traceroute, ipconfig, etc)', 
	'2. Test de velocidad', 
	'3. Diagnostico basico (ping, traceroute, ipconfig, etc)', 
	'4. Mostrar resultados de los test', 
	'5. Modificar Adaptadores de red BETA (Requiere usuario administrador)']
	choice = gui.choicebox(msg, title, choices)
	if choice == None:
		sys.exit(0)
	#print choice
	
	if choice == choices[0]:
		Completo()
	elif choice == choices[1]:
		TestVelocidad()
	elif choice == choices[2]:
		Diagnostico()
	elif choice == choices[3]:
		MuestarResultados()
	elif choice == choices[4]:
		#runRoot(nada)
		Adaptadores()
		#EnProceso()

	
	
#MuestarResultados()
#ProcesosComunes()
main()
