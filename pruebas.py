#import pywhatkit
import os
import hashlib
import base64
import calendar
import random
import math


def mensajeWhatsApp():
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


#mensajeWhatsApp()
#contraseña()
#calendario(2020)
#enteroAleatorio(0, 1)
suelo(-2/3)