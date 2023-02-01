import bs4
import requests
from pathlib import Path


url = Path('C:\programacion\python\Dia 11 Web Scraping')

# Url sin numero de pagina
urlPag = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-{}.html'

# Lista de titulos de 4 o 5 estrellas
titulos_rating_altos = []

for pagina in range(1, 51):

    # Crear sopa en cada pagina
    url_pagina = urlPag.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    
    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    for l in libros:
        # Verificar las estrellas
        if len(l.select('.star-rating.Four')) != 0 or len(l.select('.star-rating.Five')) != 0:
            # guardar titulo
            titulo_libro = l.select('a')[1]['title']

            # Agregar libros a la lista
            titulos_rating_altos.append(titulo_libro)

# ver lista de libros    
for t in titulos_rating_altos:
    print(t)


