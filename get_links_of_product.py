import requests
from bs4 import BeautifulSoup
import re
from random import randint

CATS = 'Electric%20Door%20Lock'
CAT = 'a5'


HOST = 'https://en.yiwugo.com/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36'
}
def get_html(url, params=''):
    req = requests.get(url, params=params)
    return req

def get_pagination(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', {'class':'bord_list_page'}).find_all('li', {'class':'page_no'})

    for page in pagination:
        link = page.find('a').get('href')
        lastPage = page.find('a').get_text()
        lastPage = int(lastPage) + 1
    return lastPage

def get_products_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', {'class':'product_inf'})

    linksProducts = []

    for linkProduct in products:
        linkProduct = 'https:'+linkProduct.find('a').get('href')
        linksProducts.append(linkProduct)
    
    return linksProducts


    


        url = 'https://en.yiwugo.com/search/s.html?cpage=1&queryKey='+CATS
        html = get_html(url)
        lp = get_pagination(html.text)

        for i in range(1, lp):
            i = str(i)
            url = 'https://en.yiwugo.com/search/s.html?cpage='+i+'&queryKey='+CATS
            html = get_html(url)
            data = get_products_link(html.text)

            for link in data:
                with conn.cursor() as cursor:
                    insert_query = 'INSERT INTO `'+CAT+'` (`link`) VALUES ("'+link+'")'
                    cursor.execute(insert_query)
                    conn.commit()
                    showLoading = "." * randint(0, 50)
                    print('Insert data '+showLoading)

        print('SUCCESS!!!' + CAT)

    



        



