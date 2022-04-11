import requests
from bs4 import BeautifulSoup as bs

#Función con la que obtendremos los datos de los inmuebles
def find_information(id,header):

    """
    Esta función realizará el Scrapping en la web de Idealista para obtener la siguiente información:
        ·título: str con el título de la vivienda.
        ·localizacion: str con el lugar de la vivienda.
        ·precio: int con el precio de la vivienda en euros.
        ·precio_sin_descuento: int con el precio original de la vivienda en euros.
        ·d_básica: lista de strings con los detalles básico de la vivienda.
        ·d_extra: lista de strings con algunos detalles extra de la vivienda.
        ·d_extra1: lista de strings con algunos más detalles extra de la vivienda.

    Inputs: 
        ·id: str con el id del inmueble.
        ·header: diccionario con los headers para realizar el request.
    Output:
        ·list_info: lista con las informaciones descritas anteriormente
    """
    #Realizaremos el request
    url = f'https://www.idealista.com/inmueble/{id}/'
    r = requests.get(url, headers = header)
    soup = bs(r.text,'lxml')

    #Obtendremos toda la información que queremos:
    titulo = soup.find("h1",{"class":""}).text.strip()
    localizacion = soup.find("span",{"class":"main-info__title-block"}).find("span").text.strip()
    precio = int(soup.find("div",{"class":"info-data"}).find("span",{"class":"info-data-price"}).text.replace(".","").replace("€","").strip())
    #Ver si tenemos descuento:
    try : 
        precio_sin_descuento = int(soup.find("div",{"class":"info-data"}).find("span",{"class":"pricedown"}).find("span").text.replace(".","").replace("€","").strip())
    except : 
        precio_sin_descuento = precio

    #Detalles con list comprehension
    detalle1 = soup.find ("section",{"id":"details"}).find("div",{"class":"details-property-feature-one"})
    d_basicas = [detail.text.strip() for detail in detalle1.find_all("li")]

    detalle2 = soup.find ("section",{"id":"details"}).find("div",{"class":"details-property-feature-two"})
    d_extra = [detail.text.strip() for detail in detalle2.find_all("li")]

    detalle3 = soup.find ("section",{"id":"details"}).find("div",{"class":"details-property-feature-three"})
    d_extra1 = [detail.text.strip() for detail in detalle3.find_all("li")]

    list_info = [id,titulo,localizacion,precio,precio_sin_descuento,d_basicas,d_extra,d_extra1]

    return list_info
