import requests
from bs4 import BeautifulSoup
import re


url = 'https://en.yiwugo.com/product/detail/936208049.html'

def get_html(url, params=''):
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36'
    }
    req = requests.get(url, headers=HEADERS)
    return req

def get_vendor(url):
    html = get_html(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    contacts = soup.find('div', {'class':'index_left'}).find_all('li', {'class':'fontbold'})
    
    
    if(soup.find('div', {'class':'index_left'}).find('span', {'class':'email-go'})):
        vEmail = soup.find('div', {'class':'index_left'}).find('span', {'class':'email-go'}).find('a').get_text()

    vContact = ''
    vMobile = ''
    vTel = ''
    vWC = ''

    for con in contacts:
        tmp = con.get_text()
        if('Contact' in tmp):
            vContact = tmp[9:len(tmp)-1]
        elif('Mobile' in tmp):
            vMobile = tmp[8:len(tmp)-1]
        elif('Tel' in tmp):
            vTel = tmp[4:len(tmp)-1]
        elif('WeC' in tmp):
            vWC = tmp[8:len(tmp)-1]


    dataVendor = {
                'Contanct': vContact,
                'Mobile': vMobile,
                'Tel': vTel,
                'WC': vWC,
                }

    dataVendor['email'] = vEmail

    return dataVendor



def get_product_data(url):
    html = get_html(url)
    productData = []
    soup = BeautifulSoup(html.text, 'html.parser')
    pName = soup.find('span', {'class':'font16px fontbold fontblue tit-left'}).get_text()
    pDes = soup.find('div', {'class':'pro_view_bold left'}).find('div')
    pVendor = 'https:'+soup.find('span', {'class':'fontbold fontbluelink font14px'}).find('a').get('href')
  
    productData.append({'name':pName})
    productData.append({'des':pDes})
    productData.append({'vendor':pVendor})

    pPrice = soup.find('div', {'class':'pro_view_isleft'}).find_all('tr', {'height':'27'})
    prices = []

    if pPrice == '':
        print(123)
        exit()


    print(pPrice)
    exit()

    for pr in pPrice:
        pr = pr.get_text()
        pr = ''.join(pr.split())
        pr = re.sub(r"Above", '', pr )
        price = re.search(r"￥.*/", pr)
        price = price.group(0)[1:-1]
        qty = re.search(r"[0-9]*", pr)
        qty = qty.group(0)

        prices.append({qty:price})
    
    productData.append({'prices':prices})

    allImgs = []
    imgs = soup.find('div', {'class':'pro_view_small'}).find_all('img')
    for img in imgs:
        img = img.get('bigsrc')
        allImgs.append({img})
    
    productData.append({'imgs':allImgs})



    return productData

get_product_data(url)
