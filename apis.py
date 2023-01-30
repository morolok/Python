import requests
import json
from datetime import datetime


api_key_geolocalizacion = 'd16052a12e78a581c38d93a4c166a9bd'
url_base_geolocalizacion = 'http://api.positionstack.com/v1/forward'
url_base_tiempo = 'https://api.open-meteo.com/v1/forecast'
codigos_tiempo = {0: 'Cielo claro', 1: 'Principalmente claro', 2: 'Parcialmente nublado', 4: 'Nublado', 45: 'Niebla', 
                 48: 'Depositando escarcha de niebla', 51: 'Llovizna ligera', 52: 'Llovizna moderada', 53: 'Llovizna densa', 
                 56: 'Llovizna helada ligera', 57: 'Llovizna helada intensa', 61: 'Lluvia ligera', 63: 'Lluvia moderada', 
                 65: 'Lluvia intensa', 66: 'Lluvia helada ligera', 67: 'Lluvia helada intensa', 71: 'Nieve ligera', 
                 73: 'Nieve moderada', 75: 'Nieve intensa', 77: 'Copos de nieve', 80: 'Chubascos ligeros', 
                 81: 'Chubascos moderados', 82: 'Chubascos violentos', 85: 'Chubascos de nieve ligeros', 
                 86: 'Chubascos de nieve intensos', 95: 'Tormenta eléctrica ligera o moderada', 
                 96: 'Tormenta eléctrica con granizo ligero', 99: 'Tormenta eléctrica con granizo intenso'}

def obtener_coordenadas_ciudad(ciudad, pais):
    query = ciudad + ',' + pais
    parametros = {'access_key': api_key_geolocalizacion, 'query': query}
    peticion = requests.get(url_base_geolocalizacion, params=parametros)
    respuesta_json = json.loads(peticion.text)
    numero_respuestas = len(respuesta_json['data'])
    latitud = None
    longitud = None
    #print(respuesta_json['data'])
    if(numero_respuestas == 1):
        latitud = str(respuesta_json['data'][0]['latitude'])
        longitud = str(respuesta_json['data'][0]['longitude'])
    else:
        todas_respuestas = respuesta_json['data']
        posibles_respuestas = []
        for respuesta in todas_respuestas:
            if(ciudad.lower() == respuesta['name'].lower()):
                posibles_respuestas.append(respuesta)
        if(len(posibles_respuestas) == 0):
            print('¡NO EXISTE NINGUNA COINCIDENCIA PARA LA BÚSQUEDA DE LA CIUDAD!')
        elif(len(posibles_respuestas) == 1):
            print('Una posible respesta')
        else:
            for respuesta in posibles_respuestas:
                if(not (respuesta['administrative_area'] == None) and not (respuesta['locality'] == None)):
                    if(ciudad.lower() == respuesta['administrative_area'].lower() and ciudad.lower() == respuesta['locality'].lower()):
                        latitud = str(respuesta_json['data'][0]['latitude'])
                        longitud = str(respuesta_json['data'][0]['longitude'])
                        break
                    elif(ciudad.lower() == respuesta['administrative_area'].lower()):
                        latitud = str(respuesta_json['data'][0]['latitude'])
                        longitud = str(respuesta_json['data'][0]['longitude'])
                        break
                    elif(ciudad.lower() == respuesta['locality'].lower()):
                        latitud = str(respuesta_json['data'][0]['latitude'])
                        longitud = str(respuesta_json['data'][0]['longitude'])
                        break
                    else:
                        print('¡NO HAY COINCIDENCIA!')
                elif(respuesta['administrative_area'] == None):
                    if(ciudad.lower() == respuesta['locality'].lower()):
                        latitud = str(respuesta_json['data'][0]['latitude'])
                        longitud = str(respuesta_json['data'][0]['longitude'])
                        break
                    else:
                        print('¡NO HAY COINCIDENCIA!')
                elif(respuesta['locality'] == None):
                    if(ciudad.lower() == respuesta['administrative_area'].lower()):
                        latitud = str(respuesta_json['data'][0]['latitude'])
                        longitud = str(respuesta_json['data'][0]['longitude'])
                        break
                    else:
                        print('¡NO HAY COINCIDENCIA!')
                else:
                    print('¡NO HAY COINCIDENCIA!')
    print(latitud, longitud)
    return latitud, longitud, ciudad, pais


def obtener_tiempo_actual_ciudad(latitud, longitud, ciudad, pais):
    if(latitud == None or longitud == None):
        print('No se ha encontrado una ciudad con los términos de búsqieda introducidos')
    else:
        parametros = {'latitude': latitud, 'longitude': longitud, 'windspeed_unit': 'kmh', 'temperature_unit': 'celsius', 
                    'current_weather': 'true'}
        peticion = requests.get(url_base_tiempo, params=parametros)
        respuesta_json = json.loads(peticion.text)
        temperatura = str(respuesta_json['current_weather']['temperature']) + ' °C'
        velocidad_viento = str(respuesta_json['current_weather']['windspeed']) + ' km/h'
        codigo_tiempo = respuesta_json['current_weather']['weathercode']
        print(f'Tiempo actual en %s, %s:' %(str(ciudad).upper(), str(pais).upper()))
        print('\t' + 'Temperatura: ' + temperatura)
        print('\t' + 'Velocidad del viento: ' + velocidad_viento)
        if(codigo_tiempo in codigos_tiempo.keys()):
            tiempo = codigos_tiempo.get(codigo_tiempo)
            print('\t' + 'Tiempo: ' + tiempo)


def obtener_tiempo_hoy_horas_ciudad(latitud, longitud, ciudad, pais):
    if(latitud == None or longitud == None):
        print('No se ha encontrado una ciudad con los términos de búsqieda introducidos')
    else:
        parametros = {'latitude': latitud, 'longitude': longitud, 'windspeed_unit': 'kmh', 'temperature_unit': 'celsius', 
                    'hourly': 'temperature_2m'}
        peticion = requests.get(url_base_tiempo, params=parametros)
        respuesta_json = json.loads(peticion.text)
        hora_temperatura = {}
        horas = respuesta_json['hourly']['time']
        temperaturas = respuesta_json['hourly']['temperature_2m']
        dia_hoy = int(datetime.today().day)
        #print(respuesta_json)
        for i in range(len(respuesta_json['hourly']['time'])):
            fecha_hoy = int(horas[i].split('T')[0].split('-')[2])
            if(dia_hoy == fecha_hoy):
                #print(fecha_hoy)
                hora_temperatura[horas[i].replace('T', ' ')] = str(temperaturas[i])
        #print(hora_temperatura)
        print(f'Tiempo por horas en %s, %s el día de hoy:' %(str(ciudad).upper(), str(pais).upper()))
        for c, v in hora_temperatura.items():
            print('\tTemperatura a las ' + c.split(' ')[1] + ' horas: ' + v + ' °C')
        #print(len(respuesta_json['hourly']['time']))
        #print(len(respuesta_json['hourly']['temperature_2m']))


def obtener_tiempo_mañana_horas_ciudad(latitud, longitud, ciudad, pais):
    if(latitud == None or longitud == None):
        print('No se ha encontrado una ciudad con los términos de búsqieda introducidos')
    else:
        parametros = {'latitude': latitud, 'longitude': longitud, 'windspeed_unit': 'kmh', 'temperature_unit': 'celsius', 
                    'hourly': 'temperature_2m'}
        peticion = requests.get(url_base_tiempo, params=parametros)
        respuesta_json = json.loads(peticion.text)
        hora_temperatura = {}
        horas = respuesta_json['hourly']['time']
        temperaturas = respuesta_json['hourly']['temperature_2m']
        dia_hoy = int(datetime.today().day)
        dia_mañana = 0
        for i in range(len(respuesta_json['hourly']['time'])):
            fecha_hoy = int(horas[i].split('T')[0].split('-')[2])
            if(not(dia_hoy == fecha_hoy)):
                dia_mañana = int(horas[i].split('T')[0].split('-')[2])
                break
        for i in range(len(respuesta_json['hourly']['time'])):
            fecha_mañana = int(horas[i].split('T')[0].split('-')[2])
            if(dia_mañana == fecha_mañana):
                hora_temperatura[horas[i].replace('T', ' ')] = str(temperaturas[i])
        print(f'Tiempo por horas en %s, %s mañana día %s:' %(str(ciudad).upper(), str(pais).upper(), str(dia_mañana)))
        for c, v in hora_temperatura.items():
            print('\tTemperatura a las ' + c.split(' ')[1] + ' horas: ' + v + ' °C')




#latitud, longitud, ciudad, pais= obtener_coordenadas_ciudad('tregrg', 'italiregegregra')
latitud, longitud, ciudad, pais= obtener_coordenadas_ciudad('madrid', 'españa')
obtener_tiempo_actual_ciudad(latitud, longitud, ciudad, pais)
obtener_tiempo_hoy_horas_ciudad(latitud, longitud, ciudad, pais)
obtener_tiempo_mañana_horas_ciudad(latitud, longitud, ciudad, pais)