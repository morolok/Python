palabras = []
posibles_palabras = []


def wordle_script():

    def extraer_palabras():
        # Abrir el fichero y guardar las palabras de 5 letras
        with open('diccionario.txt', 'r', encoding='utf-8') as f:
            palabras_diccionario = f.readlines()
            for p in palabras_diccionario:
                pal = p.strip()
                if(len(pal) == 5):
                    palabras.append(pal)
        f.close()

    def condiciones_palabras():
        # Añadir restricciones para filtrar las palabras y quedarnos con las que cumplan las condiciones 
        # de las letras

        # Filtrar las palabras que tengan las letras amarillas o verdes y nos las quedamos
        for pal in palabras:
            if((pal[0] == 'm') and ((pal[1] == 'e') or (pal[1] == 'é')) and (pal[2] == 'n') and 
            ((pal[3] == 'o') or (pal[3] == 'ó'))):
                posibles_palabras.append(pal)
        print(len(posibles_palabras))

        # Eliminar las palabras que no tengan las letras en gris
        seguir1 = True
        while(seguir1):
            longitud_antes = len(posibles_palabras)
            for pal in posibles_palabras:
                if('v' in pal):
                    posibles_palabras.remove(pal)
                elif(('i' in pal) or ('í' in pal)):
                    posibles_palabras.remove(pal)
                elif(('a' in pal) or ('á' in pal)):
                    posibles_palabras.remove(pal)
                elif(('u' in pal) or ('ú' in pal)):
                    posibles_palabras.remove(pal)
                elif('p' in pal):
                    posibles_palabras.remove(pal)
                elif('t' in pal):
                    posibles_palabras.remove(pal)
                elif('r' in pal):
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
                if(pal[0] == 'n'):
                    posibles_palabras.remove(pal)
                elif((pal[1] == 'o') or (pal[1] == 'ó')):
                    posibles_palabras.remove(pal)
                elif((pal[4] == 'o') or (pal[4] == 'ó')):
                    posibles_palabras.remove(pal)
            longitud_despues = len(posibles_palabras)
            if(longitud_antes == longitud_despues):
                seguir2 = False
        print(len(posibles_palabras))
        print(posibles_palabras)
    
    def empieza_palabra(inicio):
        res = []
        for pal in posibles_palabras:
            # Antes estaba con pal pero puede que sea mejor recorrer las posibles palabras
            if(pal.startswith(inicio)):
                res.append(pal)
        print(res)
    
    def termina_palabra(fin):
        res = []
        for pal in posibles_palabras:
            # Antes estaba con pal pero puede que sea mejor recorrer las posibles palabras
            if(pal.endswith(fin)):
                res.append(pal)
        print(res)        

    extraer_palabras()
    condiciones_palabras()
    #termina_palabra('risa')
    empieza_palabra('meno')


def wordle_web_scraping():
    pass

wordle_script()