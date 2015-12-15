# -*- coding: iso-8859-15 -*-
import sys  
import admin
import os
import funciones
import re
import subprocess

ruta = funciones.CreaDirectorioTrabajo()

#https://social.technet.microsoft.com/Forums/scriptcenter/en-US/e4424503-317c-44d1-8ecb-a40ad8796720/run-bat-file-in-admin-privilege
'''
Netsh interface set interface "Local Area Connection" enable
Netsh interface set interface "Local Area Connection" disable

netsh interface ip set address "Red local" static 192.168.0.3 255.255.255.0 192.168.0.1 1

netsh interface ip set dns name="Local Area Connection" static 208.67.222.222
netsh interface ip add dns name="Local Area Connection" 208.67.220.220 index=2

netsh interface ip set address "Description" dhcp
netsh interface ip set dnsservers name="Local Area Connection" source=dhcp


'''
def runRoot(funcion):

	#funcion()
	if not admin.isUserAdmin():
		#admin.runAsAdmin(cmdLine=funcion())
		admin.runAsAdmin(cmdLine=funcion())
	funcion()

def creaBat(comando='ipconfig', fichero='ip.bat'):
	f = open(fichero,'w')
	f.write(comando)
	f.close



def listaAdaptadores():
	os.system('netsh interface show interface > %s\\interfaces'%ruta)
	f = open('%s\\interfaces'%ruta, 'r')
	lista = f.read()
	f.close
	return re.findall('Conex.*|Eth.*|WI.*', lista)

def batSTATIC(adaptadores, datos):
	#adaptadores = listaAdaptadores()		# coger esta funcion en main y ponerla con interfaz grafica y mandar la interfaz como parametro a la funcion
	
	print datos
	#netsh interface ipv4 set address name = "Conexión de área local 2" source=static address=172.0.0.181 mask=255.255.255.0 gateway=172.0.0.121
	comando = '''netsh interface ipv4 set address name="%s" source=static %s %s %s 1
netsh interface ipv4 set dns name="%s" static %s
netsh interface ipv4 add dns name="%s" %s index=2'''%(adaptadores, datos[0], datos[1], datos[2], adaptadores, datos[3], adaptadores, datos[4])
	creaBat(comando)
	
	netshcmd=subprocess.Popen('ip.bat', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE )
	output, errors =  netshcmd.communicate()
	if errors: 
		print "WARNING: ", errors
	else:
		print "SUCCESS ", output	

def batDHCP(adaptadores):
	#adaptadores = listaAdaptadores()		# coger esta funcion en main y ponerla con interfaz grafica y mandar la interfaz como parametro a la funcion
	
	comando = '''netsh interface ipv4 set address "%s" dhcp
netsh interface ipv4 set dnsservers name="%s" source=dhcp'''%(adaptadores,adaptadores)
	creaBat(comando)
	
	netshcmd=subprocess.Popen('ip.bat', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE )
	output, errors =  netshcmd.communicate()
	if errors: 
		print "WARNING: ", errors
	else:
		print "SUCCESS ", output	


#batDHCP()
#batSTATIC()
