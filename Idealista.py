#Importando libreri≠as necesarias
import requests
import os
import csv
import time
import random
from bs4 import BeautifulSoup as bs
from info_casa import find_information

#Current directory where is located the script
currentDir = os.path.dirname(__file__)
filename = "idealista_info_casa.csv"
filePath = os.path.join(currentDir, filename)

#El c√≥digo postal que vamos a utilizar
cp_Sevilla = '41002'
url = f'https://www.idealista.com/buscar/venta-viviendas/{cp_Sevilla}/'

#Utilizamos headers para prevenir el bloqueo de la IP
header = dict()
header = {
    "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-ES,es;q=0.9',
    'cache-control': 'max-age=0',
    'dnt':'1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
r = requests.get(url, headers = header)
soup = bs(r.text,'lxml')
articles = soup.find("div",{"class":"container"}).find("main", {"class":"listing-items"}).find_all("article")
id_inmueble = [article.get("data-adid") for article in articles]

#Escribimos el csv para cada inmueble
with open(filePath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for id in id_inmueble:
            writer.writerow(find_information(id, header))
time.sleep(random.randint(1,3)*random.random())