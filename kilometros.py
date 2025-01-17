
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


def kms_totales_sportage(kms_totales_coche, kms_sportage):
	kmsYoSportage = sum(kms_sportage)	
	tantoPorciento = (kmsYoSportage*100)/kms_totales_coche
	tantoPorcientoString = "%.2f" % tantoPorciento
	print("El Kia Sportage tiene un total de", kms_totales_coche, "kilometros. De los cuales yo he hecho",
	kmsYoSportage, "kilometros. Es decir, el", tantoPorcientoString, "%\n")


def kms_totales_scenic(kms_totales_coche, kms_scenic):
	kmsYoScenic = sum(kms_scenic)	
	tantoPorciento = (kmsYoScenic*100)/kms_totales_coche
	tantoPorcientoString = "%.2f" % tantoPorciento
	print("El Renualt Scenic tiene un total de", kms_totales_coche, "kilometros. De los cuales yo he hecho",
	kmsYoScenic, "kilometros. Es decir, el", tantoPorcientoString, "%\n")



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

kms2020 = [3, 4, 16, 14, 13, 13, 9, 12, 19, 11, 10, 8, 24, 38, 45, 10, 71, 7, 10, 18, 6, 8, 6, 7, 7, 16, 12, 7, 6, 
	8, 13, 13, 10, 10, 35, 6, 8, 7, 7, 53, 15, 384, 395, 19, 7, 12, 34, 508, 24, 2, 7, 27, 4, 5, 17, 477, 33, 14, 
	7, 7, 11, 31, 6, 8, 6, 16, 8, 6, 7, 7, 10, 8, 32, 6, 6, 7, 12, 15, 7, 7, 10, 7, 8, 8, 15, 8, 24, 13, 13]

kms2021 = [8, 13, 5, 17, 7, 7, 6, 11, 10, 5, 7, 7, 11, 7, 7, 8, 15, 23, 15, 10, 13, 7, 15, 8, 13, 26, 6, 7, 8, 10, 7, 
	18, 7, 8, 7, 8, 7, 14, 15, 7, 30, 475, 186, 479, 475, 11, 97, 97, 8, 16, 16, 208, 481, 13, 21, 7, 28, 475, 230,
	479, 4, 6]


#Kilómetros en cada coche

kms_scenic=[100, 100, 251, 266, 411, 411, 533, 533, 533, 7, 11, 12, 13, 7, 33, 13, 11, 8, 11, 11, 18, 11, 7, 7, 
	13, 16, 11, 20, 17, 7, 14, 9, 16, 8, 311, 9, 11, 24, 12, 13, 4]

kms_sportage=[3, 9, 14, 18, 16, 13, 12, 20, 15, 8, 9, 18, 7, 12, 28, 8, 9, 23, 4, 6, 30, 29, 5, 7, 5, 7, 6, 192, 
	20, 502, 17, 11, 17, 215, 11, 9, 8, 522, 4, 5, 533, 33, 12, 17, 20, 12, 16, 15, 3, 29, 22, 65, 16, 12, 15, 17, 
	76, 11, 16, 11, 11, 17, 228, 11, 39, 533, 92, 478, 18, 7, 6, 7, 12, 12, 15, 10, 8, 20, 555, 21, 46, 11, 522, 12, 
	10, 13, 7, 16, 13, 16, 6, 18, 17, 11, 12, 8, 9, 248, 256, 7, 7, 64, 10, 23, 12, 16, 36, 26, 15, 39, 7, 474, 38, 7, 
	6, 17, 6, 37, 6, 29, 36, 7, 107, 108, 30, 73, 18, 20, 2, 31, 8, 4, 476, 18, 13, 33, 12, 18, 9, 9, 13, 11, 44, 16, 52, 
	19, 15, 13, 8, 33, 11, 21, 46, 19, 17, 11, 227, 16, 18, 11, 11, 11, 33, 16, 4, 5, 9, 22, 3, 4, 16, 14, 13, 13, 9, 12,
	19, 11, 10, 8, 24, 38, 45, 10, 71, 7, 10, 18, 6, 8, 6, 7, 7, 16, 12, 7, 6, 8, 13, 13, 10, 10, 35, 6, 8, 7, 7, 53, 15, 
	384, 395, 19, 7, 12, 34, 508, 24, 2, 7, 27, 4, 5, 17, 477, 33, 14, 7, 7, 11, 31, 6, 8, 6, 16, 8, 6, 7, 7, 10, 8, 32, 
	6, 6, 7, 12, 15, 7, 7, 10, 7, 8, 8, 15, 8, 24, 13, 13, 8, 13, 5, 17, 7, 7, 6, 11, 10, 5, 7, 7, 11, 7, 7, 8, 15, 23, 
	15, 10, 13, 7, 15, 8, 13, 26, 6, 7, 8, 10, 7, 18, 7, 8, 7, 8, 7, 14, 15, 7, 30, 475, 186, 479, 475, 11, 97, 97, 8, 
	16, 16, 208, 481, 13, 21, 7, 28, 475, 230, 479, 4, 6]

#Adición de datos al diccionario

añadirAñoAlDiccionario(kilometros, 2017)

añadirAñoAlDiccionario(kilometros, 2018)

añadirAñoAlDiccionario(kilometros, 2019)

añadirAñoAlDiccionario(kilometros, 2020)

añadirAñoAlDiccionario(kilometros, 2021)

añadirKilometroAlAño(kilometros, 2017, kms2017)

añadirKilometroAlAño(kilometros, 2018, kms2018)

añadirKilometroAlAño(kilometros, 2019, kms2019)

añadirKilometroAlAño(kilometros, 2020, kms2020)

añadirKilometroAlAño(kilometros, 2021, kms2021)

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

print("Kilometros recorridos con el Kia Sportage 2018:", sum(kms_sportage), "\n")

# Cambiar los km totales del coche cada vez que se ejecute el archivo

kms_totales_sportage(28002, kms_sportage)

kms_totales_scenic(58519, kms_scenic)