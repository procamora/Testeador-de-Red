# const_output.py
import sys, os
from subprocess import PIPE, Popen
import funciones

ruta = funciones.CreaDirectorioTrabajo()

def EjecutaComando(comando, host):

	cmd_line = '%s %s'%(comando,host)

	proceso = Popen(cmd_line, stdout=PIPE)

	#error_encontrado = proceso.stderr.read()
	listado = proceso.stdout.read()
	proceso.stdout.close()
	#print listado 
	#proceso.communicate()[0]
	'''
	if not error_encontrado: 
		print listado 
	else: 
		print "Se produjo el siguiente error:\n%s" % error_encontrado
	'''
	#ruta = funciones.CreaDirectorioTrabajo()
	f=open('%s\\%s.github'%(ruta,comando), 'a')
	f.write(listado.replace('\n',''))
	f.write('*********************************\n')
	f.close()
	

def main():
	#funciones.LimpiaDirectorio(ruta)
	#se pone los espacios a la hora de crearlos para que todos tengan la misma longitud y luego se generen los ficheros bien
	ope=['ping    8.8.8.8', 'ping    -l 10000 github.es', 'ping    google.es', 'tracert 8.8.8.8', 'tracert google.es', 'route   print', 'ipconfig /all']
	for i in ope:
		rutaCompleta = '%s\\%s.github'%(ruta,i[:8].replace(' ',''))
		funciones.BoraFichero(rutaCompleta)

	for i in ope:
		#print '%s | %s'%(i[:8].replace(' ',''),i[8:])
		EjecutaComando(i[:8].replace(' ',''),i[8:])




#main()
