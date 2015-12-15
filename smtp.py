import mailer
import funciones
ruta = funciones.CreaDirectorioTrabajo()

def main(adjuntos=''):
	message = mailer.Message()
	nombreCorreo = 'diagnosticos@procamora.es'
	message.From = 'Diagnostico procamora <%s>'%nombreCorreo
	message.To = 'USERNAME@procamora.es'
	message.Subject = 'Diagnostico procamora'
	message.Html = open('letter.txt', 'rb').read()
	if len(adjuntos) != 0:
		message.attach(adjuntos)
	#message.attach('github.zip')
	mail = mailer.Mailer('ssl0.ovh.net')
	#Ff6utF0Dsh
	mail.login(nombreCorreo,funciones.CreaPalabra())
	mail.send(message)



