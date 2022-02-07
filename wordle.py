palabras = []
posibles_palabras = []

def extraer_palabras():
    with open('diccionario.txt', 'r', encoding='utf-8') as f:
        palabras_diccionario = f.readlines()
        for p in palabras_diccionario:
            pal = p.strip()
            if(len(pal) == 5):
                palabras.append(pal)
    f.close()

def condiciones_palabras():
    # Filtrar las palabras que tengan o no letras y nos las quedamos
    for pal in palabras:
        if(('o' in pal or 'ó' in pal) and ('a' in pal or 'á' in pal) and ('v' in pal) and 
        ('n' not in pal) and ('i' not in pal) and ('í' not in pal)):
            posibles_palabras.append(pal)
    print(len(posibles_palabras))
    # Filtrar de las posibles las palabras con letras en la posición
    for pal in posibles_palabras:
        if(not pal[1] == 'o'):
            posibles_palabras.remove(pal)
        elif(not pal[1] == 'ó'):
            posibles_palabras.remove(pal)
    print(len(posibles_palabras))
    print(posibles_palabras)


extraer_palabras()
condiciones_palabras()