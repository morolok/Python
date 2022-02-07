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
    for pal in palabras:
        if('n' not in pal and ('o' not in pal or 'ó' not in pal) and 'v' not in pal and ('i' not in pal or 'í' not in pal)):
            posibles_palabras.append(pal)
        elif('n' not in pal or ('o' not in pal or 'ó' not in pal) or 'v' not in pal or ('i' not in pal or 'í' not in pal)):
            posibles_palabras.append(pal)
            print(pal)
        elif('n' not in pal):
            posibles_palabras.append(pal)
        elif('o' not in pal or 'ó' not in pal):
            posibles_palabras.append(pal)
        elif('v' not in pal):
            posibles_palabras.append(pal)
        elif('i' not in pal or 'í' not in pal):
            posibles_palabras.append(pal)
        
        elif(pal[4] == 'a' or pal[4] == 'á'):
            posibles_palabras.append(pal)
    
    #print(posibles_palabras)


extraer_palabras()
condiciones_palabras()