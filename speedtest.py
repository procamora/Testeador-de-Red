import os

import funciones

ruta = funciones.CreaDirectorioTrabajo()


def main(server='1652'):
    #funciones.LimpiaDirectorio(ruta)
    # si no tengo conexion ver que error da
    fichero = '%s\\speedtest.github'%ruta
    funciones.BoraFichero(fichero)
    comando = 'speedtest_cli.exe --server %s > %s'%(server,fichero)
    #comando = 'help'
    res = os.system(comando)
    print(res)
    if res == 1:
        f = open(fichero, 'a')
        f.write('Fallo al hacer el test de velocidad')
        f.close


#main()
