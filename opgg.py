import urllib.request
import webbrowser
from bs4 import BeautifulSoup
from tabulate import tabulate


url = 'https://euw.op.gg/champion/statistics'
path_chrome = 'C:\Program Files (x86)\Google\Chrome\Application'
#positions = {'Top': 'TOP', 'Jungla': 'JUNGLE', 'Medio': 'MID', 'Adc': 'ADC', 'Support': 'SUPPORT'}
top, jungle, mid, adc, support = {}, {}, {}, {}, {}
tableTop, tableJungle, tableMid, tableAdc, tableSupport = [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']]
listTop, listJungle, listMid, listAdc, listSupport = [], [], [], [], []


def readWebsite():
    file = urllib.request.urlopen(url)
    soup = BeautifulSoup(file, "lxml")
    ls = soup.find('table', class_='champion-index-table tabItems')
    for x in ls.find('tbody', class_='tabItem champion-trend-tier-TOP').find_all('tr'):
        listTop.append(x)
    for x in ls.find('tbody', class_='tabItem champion-trend-tier-JUNGLE').find_all('tr'):
        listJungle.append(x)
    for x in ls.find('tbody', class_='tabItem champion-trend-tier-MID').find_all('tr'):
        listMid.append(x)
    for x in ls.find('tbody', class_='tabItem champion-trend-tier-ADC').find_all('tr'):
        listAdc.append(x)
    for x in ls.find('tbody', class_='tabItem champion-trend-tier-SUPPORT').find_all('tr'):
        listSupport.append(x)


def loadTop():
    for campeon in listTop:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        top[(ranking, name)] = [name, level, link]
        tableTop.append([ranking, name, level, link])


def loadJungle():
    for campeon in listJungle:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        jungle[(ranking, name)] = [name, level, link]
        tableJungle.append([ranking, name, level, link])


def loadMid():
    for campeon in listMid:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        mid[(ranking, name)] = [name, level, link]
        tableMid.append([ranking, name, level, link])


def loadAdc():
    for campeon in listAdc:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        adc[(ranking, name)] = [name, level, link]
        tableAdc.append([ranking, name, level, link])


def loadSupport():
    for campeon in listSupport:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        support[(ranking, name)] = [name, level, link]
        tableSupport.append([ranking, name, level, link])
        

def main():
    bucle = True
    while(True):
        print('Elige línea entre: Top, Jungle, Mid, Adc, Support. Si desea salir escribe salir.')
        position = input()
        if(position.lower() == 'top'):
            readWebsite()
            loadTop()
            print('Campeones de Top')
            print(tabulate(tableTop, headers='firstrow', tablefmt='fancy_grid'))
            while(True):
                print('Elige el campeón que deseas jugar escribiendo el nombre. Si desea salir escribe salir.')
                findChampion = False
                champion = input()
                if(champion.lower() == 'salir'):
                    break
                for c, v in top.items():
                    if(champion.lower() == c[1].lower()):
                        findChampion = True
                        webbrowser.open(v[2])
                        break
                if(findChampion == True):
                    break
                else:
                    print('El campeón introducido no es correcto, introdúcelo de nuevo')
            break
        elif(position.lower() == 'jungle'):
            readWebsite()
            loadJungle()
            print('Campeones de Jungla')
            print(tabulate(tableJungle, headers='firstrow', tablefmt='fancy_grid'))
            while(True):
                print('Elige el campeón que deseas jugar escribiendo el nombre. Si desea salir escribe salir.')
                findChampion = False
                champion = input()
                if(champion.lower() == 'salir'):
                    break
                for c, v in jungle.items():
                    if(champion.lower() == c[1].lower()):
                        findChampion = True
                        webbrowser.open(v[2])
                        break
                if(findChampion == True):
                    break
                else:
                    print('El campeón introducido no es correcto, introdúcelo de nuevo')
            break
        elif(position.lower() == 'mid'):
            readWebsite()
            loadMid()
            print('Campeones de Mid')
            print(tabulate(tableMid, headers='firstrow', tablefmt='fancy_grid'))
            while(True):
                print('Elige el campeón que deseas jugar escribiendo el nombre. Si desea salir escribe salir.')
                findChampion = False
                champion = input()
                if(champion.lower() == 'salir'):
                    break
                for c, v in mid.items():
                    if(champion.lower() == c[1].lower()):
                        findChampion = True
                        webbrowser.open(v[2])
                        break
                if(findChampion == True):
                    break
                else:
                    print('El campeón introducido no es correcto, introdúcelo de nuevo')
            break
        elif(position.lower() == 'adc'):
            readWebsite()
            loadAdc()
            print('Campeones de Adc')
            print(tabulate(tableAdc, headers='firstrow', tablefmt='fancy_grid'))
            while(True):
                print('Elige el campeón que deseas jugar escribiendo el nombre. Si desea salir escribe salir.')
                findChampion = False
                champion = input()
                if(champion.lower() == 'salir'):
                    break
                for c, v in adc.items():
                    if(champion.lower() == c[1].lower()):
                        findChampion = True
                        webbrowser.open(v[2])
                        break
                if(findChampion == True):
                    break
                else:
                    print('El campeón introducido no es correcto, introdúcelo de nuevo')
            break
        elif(position.lower() == 'support'):
            readWebsite()
            loadSupport()
            print('Campeones de Support')
            print(tabulate(tableSupport, headers='firstrow', tablefmt='fancy_grid'))
            while(True):
                print('Elige el campeón que deseas jugar escribiendo el nombre. Si desea salir escribe salir.')
                findChampion = False
                champion = input()
                if(champion.lower() == 'salir'):
                    break
                for c, v in support.items():
                    if(champion.lower() == c[1].lower()):
                        findChampion = True
                        webbrowser.open(v[2])
                        break
                if(findChampion == True):
                    break
                else:
                    print('El campeón introducido no es correcto, introdúcelo de nuevo')
            break
        elif(position.lower() == 'salir'):
            break
        else:
            print('La posición introducida no es correcta, introdúcela de nuevo.')


main()

#print(tabulate(tableTop, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableJungle, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableMid, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableAdc, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableSupport, headers='firstrow', tablefmt='fancy_grid'))