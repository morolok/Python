import os
import shutil
import hashlib
import base64
import calendar
import random
import math
import numpy as np
from fractions import Fraction
from PIL import Image


def mensajeWhatsApp():
	import pywhatkit
	pywhatkit.sendwhatmsg("+34672650155", "Mensaje de prueba a mi mismo desde python", 23, 14)


def contraseña():
	salt = os.urandom(64)
	contraseña1 = hashlib.pbkdf2_hmac('sha256', '123'.encode('utf-8'), salt, 1, dklen=128).hex()
	print("Salt:", salt)
	print()
	print("Contraseña 123 cifrada:", contraseña1)
	print()
	token = base64.b64encode(salt).decode('utf-8')
	salt2 = base64.b64decode(token)
	print("Token (Salt codificada en texto):", token)
	print()
	print("Salt decodificada del token (Debe ser igual a la Salt original):", salt2)
	print()
	contraseña2 = hashlib.pbkdf2_hmac('sha256', '123'.encode('utf-8'), salt2, 1, dklen=128).hex()
	print("Contraseña 123 cifrada con la segunda Salt (Debe ser igual a la contraseña cifrada):", contraseña2)
	print()


def calendario(year):
	print(calendar.calendar(year))


def enteroAleatorio(minim, maxim):
	print(random.randint(minim, maxim))


def suelo(num):
	print(math.floor(num))


def techo(num):
	print(math.ceil(num))


def pruebasNone():
	usuario = "carmatbla"
	if(usuario):
		print("Hay un usuario")
	usuario = None
	if(not usuario):
		print("No hay usuario")


def aristas():
	k = 1
	res = []
	for i in range(1, 11):
		j = (i+k+1)%10
		if(1<=j and j<=10):
			arista = (i, j)
			res.append(arista)
	for i in range(1, 11):
		#j = (3*k - i)%4
		j = ((3*k) %4)-i
		if(1<=j and j<=10):
			arista = (i, j)
			res.append(arista)
	print(res)
	#return res


def van(cn, i, años):
	c0 = sum([cn/(1+i)**n for n in range(1, años+1)])
	print(c0)


def ecuacion_grado_2(a, b, c):
	raiz = b**2 - 4*a*c
	if(raiz >= 0):
		x1 = (-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a)
		x2 = (-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a)
		print(x1)
		print(x2)
	else:
		print('No tiene raices reales')


def redimesion(nombre_imagen):
	imagen = Image.open(nombre_imagen)
	#newsize = (1080, 1080)
	imagen_subir = imagen.resize((1080, 1080))
	imagen_subir.save('Ingenio_42_portada_redimensionada.png')
	imagen.close()
	imagen_subir.close()
	imagen = None
	imagen_subir = None


def postInstagram():
	from instabot import Bot
	dir = 'config'
	if(os.path.exists(dir)):
		try:
			shutil.rmtree(dir)
		except OSError as e:
			print("Error: %s - %s." % (e.filename, e.strerror))
	bot = Bot()
	bot.login(username = 'antalumnosetsi', password = 'Antalumnos2020')
	#redimesion('Ingenio_42_portada.png')
	bot.upload_photo('Ingenio_42_portada_redimensionada.png', caption = 'Ya está disponible el nuevo número de la Revista Ingenio, ¡Ven a verlo!')
	if(os.path.exists(dir)):
		try:
			shutil.rmtree(dir)
		except OSError as e:
			print("Error: %s - %s." % (e.filename, e.strerror))


#mensajeWhatsApp()
#contraseña()
#calendario(2020)
#enteroAleatorio(0, 1)
#suelo(-1.5)
#pruebasNone()
#aristas()
#van(2000, 0.035, 5)
#ecuacion_grado_2(1, 7, 10)
#ecuacion_grado_2(1, -12, 20)
#ecuacion_grado_2(1, 1, -56)
#postInstagram()