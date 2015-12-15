import zipfile
import glob
import funciones
import sys
import tarfile

ruta = funciones.CreaDirectorioTrabajo()

def main():
	FicheroZip = '%s\\github.zip'%ruta
	funciones.BoraFichero(FicheroZip)
	zf = zipfile.ZipFile(FicheroZip, mode='a')

	lista = glob.glob("%s\\*.github"%ruta)
	try:
		for i in lista:
			#zf.write(i) # ruta ichero y nombre con el que se guarda, este ultimo solo cojo el nombre, no los directorios
			zf.write(i,i.split('\\')[-1], compress_type=zipfile.ZIP_DEFLATED) # ruta ichero y nombre con el que se guarda, este ultimo solo cojo el nombre, no los directorios
	finally:
		print 'finalmente'
		zf.close()
	return FicheroZip


def ComprimeTar():
	FicheroTar = '%s\\github.tar.bz2'%ruta
	funciones.BoraFichero(FicheroTar)
	tar = tarfile.open(FicheroTar, 'w')
	#tar = tarfile.open(FicheroTar, 'w:bz2')

	lista = glob.glob("%s\\*.github"%ruta)
	try:
		for i in lista:
			#tar.write(i) # ruta ichero y nombre con el que se guarda, este ultimo solo cojo el nombre, no los directorios
			tar.add(i, i.split('\\')[-1]) # ruta ichero y nombre con el que se guarda, este ultimo solo cojo el nombre, no los directorios
	finally:
		#print 'finalmente'
		tar.close()
	return FicheroTar


#ComprimeTar()
