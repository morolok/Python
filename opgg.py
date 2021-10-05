from bs4 import BeautifulSoup
import urllib.request
from tabulate import tabulate


url = 'https://euw.op.gg/champion/statistics'
#positions = {'Top': 'TOP', 'Jungla': 'JUNGLE', 'Medio': 'MID', 'Adc': 'ADC', 'Support': 'SUPPORT'}
#top, jungle, mid, adc, support = {}, {}, {}, {}, {}
tableTop, tableJungle, tableMid, tableAdc, tableSupport = [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']], [['Ranking', 'Name', 'Level', 'Link']]


def cargarDatos():
    file = urllib.request.urlopen(url)
    soup = BeautifulSoup(file, "lxml")
    lista = soup.find('table', class_='champion-index-table tabItems')
    listTop = lista.find('tbody', class_='tabItem champion-trend-tier-TOP').find_all('tr')
    listJungle = lista.find('tbody', class_='tabItem champion-trend-tier-JUNGLE').find_all('tr')
    listMid = lista.find('tbody', class_='tabItem champion-trend-tier-MID').find_all('tr')
    listAdc = lista.find('tbody', class_='tabItem champion-trend-tier-ADC').find_all('tr')
    listSupport = lista.find('tbody', class_='tabItem champion-trend-tier-SUPPORT').find_all('tr')

    for campeon in listTop:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        #top[(ranking, name)] = [name, level, link]
        tableTop.append([ranking, name, level, link])
    
    for campeon in listJungle:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        #jungle[(ranking, name)] = [name, level, link]
        tableJungle.append([ranking, name, level, link])
    
    for campeon in listMid:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        #mid[(ranking, name)] = [name, level, link]
        tableMid.append([ranking, name, level, link])
    
    for campeon in listAdc:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        #adc[(ranking, name)] = [name, level, link]
        tableAdc.append([ranking, name, level, link])
    
    for campeon in listSupport:
        ranking = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--rank').text
        name = campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a').find('div', class_='champion-index-table__name').text
        link = url[0:17] + campeon.find('td', class_='champion-index-table__cell champion-index-table__cell--champion').find('a')['href'] + '/build'
        level = campeon.find_all('td', class_='champion-index-table__cell champion-index-table__cell--value')[2].find('img')['src'][64]
        #support[(ranking, name)] = [name, level, link]
        tableSupport.append([ranking, name, level, link])
        


cargarDatos()
#print(tabulate(tableTop, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableJungle, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableMid, headers='firstrow', tablefmt='fancy_grid'))
#print(tabulate(tableAdc, headers='firstrow', tablefmt='fancy_grid'))
print(tabulate(tableSupport, headers='firstrow', tablefmt='fancy_grid'))