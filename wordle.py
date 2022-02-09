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
            if(((pal[4] == 'o') or (pal[4] == 'ó')) and ((pal[1] == 'e') or (pal[1] == 'é')) and (pal[0] == 's')):
                posibles_palabras.append(pal)
        print(len(posibles_palabras))

        # Eliminar las palabras que no tengan las letras en gris
        for i in range(15):
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
                elif('q' in pal):
                    posibles_palabras.remove(pal)
                elif('u' in pal):
                    posibles_palabras.remove(pal)
                elif('ú' in pal):
                    posibles_palabras.remove(pal)
                elif('d' in pal):
                    posibles_palabras.remove(pal)
                elif('l' in pal):
                    posibles_palabras.remove(pal)
        print(len(posibles_palabras))
        
        # Eliminar las palabras que tengan letras en posicion amarilla
        for i in range(5):
            pass
            for pal in posibles_palabras:
                pass
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