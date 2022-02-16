from math import remainder
from os import remove
from turtle import pos


palabras = []
posibles_palabras = []


def wordle_script():

    def extraer_palabras():
        with open('diccionario.txt', 'r', encoding='utf-8') as f:
            palabras_diccionario = f.readlines()
            for p in palabras_diccionario:
                pal = p.strip()
                if(len(pal) == 5):
                    palabras.append(pal)
        f.close()

    def condiciones_palabras():
        # Filtrar las palabras que tengan las letras amarillas o verdes y nos las quedamos
        for pal in palabras:
            if((pal[2] == 'r') and ((pal[1] == 'u') or (pal[1] == 'ú')) and ((pal[4] == 'o') or (pal[4] == 'ó'))):
                posibles_palabras.append(pal)
        print(len(posibles_palabras))

        # Eliminar las palabras que no tengan las letras en gris        
        seguir1 = True
        while(seguir1):
            longitud_antes = len(posibles_palabras)
            for pal in posibles_palabras:
                if('n' in pal):
                    posibles_palabras.remove(pal)
                elif('v' in pal):
                    posibles_palabras.remove(pal)
                elif('i' in pal):
                    posibles_palabras.remove(pal)
                elif('í' in pal):
                    posibles_palabras.remove(pal)
                elif('a' in pal):
                    posibles_palabras.remove(pal)
                elif('á' in pal):
                    posibles_palabras.remove(pal)
                elif('t' in pal):
                    posibles_palabras.remove(pal)
                elif('e' in pal):
                    posibles_palabras.remove(pal)
                elif('é' in pal):
                    posibles_palabras.remove(pal)
                elif('m' in pal):
                    posibles_palabras.remove(pal)
                elif('b' in pal):
                    posibles_palabras.remove(pal)
            longitud_despues = len(posibles_palabras)
            if(longitud_antes == longitud_despues):
                seguir1 = False
        print(len(posibles_palabras))

        # Eliminar las palabras que tengan letras en posicion amarilla 
        seguir2 = True
        while(seguir2):
            longitud_antes = len(posibles_palabras)
            for pal in posibles_palabras:
                pass
            longitud_despues = len(posibles_palabras)
            if(longitud_antes == longitud_despues):
                seguir2 = False
        print(len(posibles_palabras))
        
        print(posibles_palabras)
    
    def termina_palabra():
        for pal in palabras:
            if(pal.endswith('risa')):
                print(pal)
        

    extraer_palabras()
    condiciones_palabras()
    #termina_palabra()


def wordle_web_scraping():
    pass

wordle_script()