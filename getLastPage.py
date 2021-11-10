from bs4 import BeautifulSoup
import requests
import re


def get_html(url):
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    r = requests.get(url, headers=HEADERS)
    return r

def get_last_page(html):
    
    data = BeautifulSoup(html, 'html.parser')
    data = data.find_all('li', {'class': 'page_no'})
    lastPage = ''

    for p in data:
        lastPage = int(p.find('a').get_text()) + 1
    
    if lastPage != '':
        return lastPage
    else:
        return 1
    



def get_products_link(url):
    r = get_html(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    products = soup.find_all('div', {'class':'product_inf'})

    productsData = []

    for product in products:
        prod = []

        link = 'https:'+product.find('a').get('href')
        prod.append(link)

        code = re.sub('//en.yiwugo.com/product/detail/', "", product.find('a').get('href'))
        code = re.sub('.html', "", code)

        prod.append(code)
        prod.append(link)

        productsData.append(prod)
    
    return productsData

def get_lp(url):
    r = get_html(url)
    lp = get_last_page(r.text)
    return lp