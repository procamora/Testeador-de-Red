import os
import glob
import wmi
import gui
import sys

def CreaDirectorioTrabajo(directorio = 'github'):
	ruta = '%s\\%s'%(os.environ['LOCALAPPDATA'],directorio)
	if not os.path.exists(ruta):
		os.mkdir(ruta)
	return ruta


def BoraFichero(rutaCompleta):
	if os.path.exists(rutaCompleta):
		print 'borrado: '+rutaCompleta
		os.remove(rutaCompleta)
		
	def EstableceCliente():
		pass

def LimpiaDirectorio(rutaCompleta):
	lista = glob.glob("%s\\*.github"%rutaCompleta)
	try:
		for i in lista:
			if os.path.exists(i):
				os.remove(i)
	except:
		pass

'''
def CreaLista(palabra):
	l = []
	for i in palabra:
		l.append(ord(i))
	return l
'''
	
def CreaPalabra(num=list()):
#def CreaPalabra(num=['','']):
	num = [70, 102, 54, 117, 116, 70, 48, 68, 115, 104]
	palabra=''
	for i in num:
		palabra=palabra+chr(i)
	#print palabra
	return palabra


def ipWMI():
	wmiService = wmi.WMI()
	colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

	if len(colNicConfigs) < 1:
		print "Can not get network configuration"
		exit()

	objNicConfig = colNicConfigs[0]
	datos = {'ip': objNicConfig.IPAddress[0],
			'subnet': objNicConfig.IPSubnet[0],
			'gateway': objNicConfig.DefaultIPGateway[0],
			'gatewayCostMetrics': 1,
			'dnsServers1': objNicConfig.DNSServerSearchOrder[0],
			'dnsServers2': objNicConfig.DNSServerSearchOrder[1],
	}
	return datos

