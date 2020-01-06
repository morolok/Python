
#Métodos para añadir datos al diccionario


def añadirAñoAlDiccionario(diccionario, año):

	if(año in diccionario.keys()):
		print("El año", año, "ya esta en el diccionario y no se puede volver a añadir.\n")
	else:
		diccionario[año] = []


def añadirKilometroAlAño(diccionario, año, listaKilometros):

	if(año not in diccionario.keys()):
		print("El año", año, "no esta en el diccionario.")
	else:
		if(len(diccionario[año])==0):
			diccionario[año] = diccionario[año] + listaKilometros
		else:
			print("Ya hay una lista de kilómetros en el año", año, "y no se puede añadir otra.\n")


#Métodos para minar datos del diccionario


def sumaDeKilometrosPorAño(diccionario, año):

	suma = sum(diccionario[año])
	return suma


def numeroDeViajesPorAño(diccionario, año):

	viajes = len(diccionario[año])
	return viajes


def obtenerViajeMasLargoDeUnAño(diccionario, año):

	distancia = max(diccionario[año])
	return distancia


#Métodos para imprimir los datos del diccionario


def imprimirDiccionario(diccionario):

	for c in diccionario:
		print(c,":", diccionario[c])
	print()


def imprimirSumaDeKilometrosDeCadaAño(diccionario):

	for c in diccionario.keys():
		suma = sumaDeKilometrosPorAño(diccionario, c)
		print("En el año", c, "el número total de kilómetros hechos es de", suma)
	print()


def imprimirMediaDeKilometrosPorViaje(diccionario):

	for c in diccionario.keys():
		suma = sumaDeKilometrosPorAño(diccionario, c)
		viajes = numeroDeViajesPorAño(diccionario, c)
		media = suma/viajes
		print("En el año", c, "la media de kilómetros por viaje es de", media)
	print()


def imprimirViajesPorCadaAño(diccionario):

	for c in diccionario.keys():
		viajes = numeroDeViajesPorAño(diccionario, c)
		print("En el año", c, "el número de viajes ha sido de", viajes)
	print()


def imprimirViajesMasLargosPorCadaAño(diccionario):

	for c in diccionario.keys():
		distancia = obtenerViajeMasLargoDeUnAño(diccionario, c)
		print("En el año", c, "el viaje más largo ha sido de", distancia, "kilómetros.")
	print()


def imprimirKilometrosPorCadaDiaDelAño(diccionario):

	for c in diccionario.keys():
		kms = sumaDeKilometrosPorAño(diccionario, c)/365
		print("En el año", c, "el número de kilómetros hechos cada día del año es de", kms)
	print()


def imprimirViajeMasLargoDeTodos(diccionario):

	maximo = 0
	año = 0
	for c in diccionario.keys():
		kms = obtenerViajeMasLargoDeUnAño(diccionario, c)
		if(kms >= maximo):
			maximo = kms
			año = c
	print("El viaje más largo de todos ha sido en el año",año ,"y el número de kilómetros fue de", maximo,'\n')


def imprimirKmsTotales(diccionario):

	acum = 0
	for c in diccionario.keys():
		acum = acum + sumaDeKilometrosPorAño(diccionario, c)
	print("Número total de kilometros realizados en coche:", acum, '\n')

kilometros = {}


#Adición de años y kilometros hechos en los respectivos años

kms2017 = [100, 100, 251, 266, 411, 411, 533, 533, 533]

kms2018 = [7, 11, 12, 13, 7, 33, 13, 11, 8, 11, 11, 18, 11, 7, 7, 13, 16, 11, 20, 17, 7, 14, 9, 16, 8, 311, 9, 
	11, 24, 12, 13, 4, 3, 9, 14, 18, 16, 13, 12, 20, 15, 8, 9, 18, 7, 12, 28, 8, 9, 23, 4,6, 30, 29, 5, 7, 5, 
	7, 6, 192, 20, 502, 17, 11, 17, 215, 11, 9, 8, 522, 4, 5, 533, 33, 12, 17, 20, 12, 16, 15, 3, 29, 22, 65, 
	16, 12, 15, 17, 76, 11, 16, 11, 11, 17, 228, 11, 39, 533, 92, 478, 18]

kms2019 = [7, 6, 7, 12, 12, 15, 10, 8, 20, 555, 21, 46, 11, 522, 12, 10, 13, 7, 16, 13, 16, 6, 18,17, 11, 12, 8, 
	9, 248, 256, 7, 7, 64, 10, 23, 12, 16, 36, 26, 15, 39, 7, 474, 38, 7, 6, 17, 6, 37, 6, 29, 36, 7, 107, 108, 30,
	73, 18, 20, 2, 31, 8, 4, 476, 18, 13, 33, 12, 18, 9, 9, 13, 11, 44, 16, 52, 19, 15, 13, 8, 33, 11, 21, 46, 19,
	17, 11, 227, 16, 18, 11, 11, 11, 33, 16, 4, 5, 9, 22]

kms2020 = [3, 4, 16]


#Kilómetros en cada coche

kms_scenic=[100, 100, 251, 266, 411, 411, 533, 533, 533, 7, 11, 12, 13, 7, 33, 13, 11, 8, 11, 11, 18, 11, 7, 7, 
	13, 16, 11, 20, 17, 7, 14, 9, 16, 8, 311, 9, 11, 24, 12, 13, 4]

kms_sportage=[3, 9, 14, 18, 16, 13, 12, 20, 15, 8, 9, 18, 7, 12, 28, 8, 9, 23, 4, 6, 30, 29, 5, 7, 5, 7, 6, 192, 
	20, 502, 17, 11, 17, 215, 11, 9, 8, 522, 4, 5, 533, 33, 12, 17, 20, 12, 16, 15, 3, 29, 22, 65, 16, 12, 15, 17, 
	76, 11, 16, 11, 11, 17, 228, 11, 39, 533, 92, 478, 18, 7, 6, 7, 12, 12, 15, 10, 8, 20, 555, 21, 46, 11, 522, 12, 
	10, 13, 7, 16, 13, 16, 6, 18, 17, 11, 12, 8, 9, 248, 256, 7, 7, 64, 10, 23, 12, 16, 36, 26, 15, 39, 7, 474, 38, 7, 
	6, 17, 6, 37, 6, 29, 36, 7, 107, 108, 30, 73, 18, 20, 2, 31, 8, 4, 476, 18, 13, 33, 12, 18, 9, 9, 13, 11, 44, 16, 52, 
	19, 15, 13, 8, 33, 11, 21, 46, 19, 17, 11, 227, 16, 18, 11, 11, 11, 33, 16, 4, 5, 9, 22, 3, 4, 16]

#Adición de datos al diccionario

añadirAñoAlDiccionario(kilometros, 2017)

añadirAñoAlDiccionario(kilometros, 2018)

añadirAñoAlDiccionario(kilometros, 2019)

añadirAñoAlDiccionario(kilometros, 2020)

añadirKilometroAlAño(kilometros, 2017, kms2017)

añadirKilometroAlAño(kilometros, 2018, kms2018)

añadirKilometroAlAño(kilometros, 2019, kms2019)

añadirKilometroAlAño(kilometros, 2020, kms2020)

#Visualización del diccionario con los métodos

imprimirDiccionario(kilometros)

imprimirSumaDeKilometrosDeCadaAño(kilometros)

imprimirMediaDeKilometrosPorViaje(kilometros)

imprimirViajesPorCadaAño(kilometros)

imprimirViajesMasLargosPorCadaAño(kilometros)

imprimirKilometrosPorCadaDiaDelAño(kilometros)

imprimirViajeMasLargoDeTodos(kilometros)

imprimirKmsTotales(kilometros)


print("Kilometros recorridos con el Renault Scenic Clase 3 Dynamic:", sum(kms_scenic), "\n")

print("Kilometros recorridos con el Kia Sportage:", sum(kms_sportage), "\n")


def kms_totales_sportage(kms_totales_coche):

	kmsYoSportage = sum(kms_sportage)	
	tantoPorciento = (kmsYoSportage*100)/kms_totales_coche
	tantoPorcientoString = "%.2f" % tantoPorciento
	print("El Kia Sportage tiene un total de", kms_totales_coche, "kilometros. De los cuales yo he hecho",
	kmsYoSportage, "kilometros. Es decir, el", tantoPorcientoString, "%\n")

# Cambiar los km totales del coche cada vez que se ejecute el archivo

kms_totales_sportage(13093)