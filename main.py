from db import get_query, ins_query
from createData import get_vendor, get_product_data
import html
import re

category = 'A1'

data = get_query('SELECT * FROM '+category+';')

ins_query('CREATE TABLE IF NOT EXISTS a_'+category+' (id int(12) NOT NULL AUTO_INCREMENT, code VARCHAR(50) NOT NULL, url VARCHAR(400) NOT NULL, name VARCHAR(500), description mediumblob, price1 varchar(60), price2 varchar(60), price3 varchar(60), img1 varchar(500), img2 varchar(500), img3 varchar(500), img4 varchar(500), vendor varchar(100), PRIMARY KEY (id));')


url = 'https://en.yiwugo.com/product/detail/936208049.html'

for d in data:
    idP = d[0]
    urlP = d[1]
    codeP = d[2]

    # Получаем всю необходимую информацию по товару
    productData = get_product_data(url)

    print(productData)
    exit()

    nameP = productData[0]['name']
    desP = productData[1]['des']

    desP = desP.repalce("&amp;", " ")


    vendorURL = productData[2]['vendor']

    priceP = productData[3]['prices']
    for pr in priceP:
        for k, v in pr.items():
            qty = k
            price = v
            print(qty)
            print(price)
    
    exit()

    
    imgsP = productData[4]['imgs']
    for im in imgsP:
        for img in im:
            img = 'http'+img

    # Получаем всю необходимую информацию по продавцу
    vendorData = get_vendor(vendorURL)

    contactV = vendorData['Contanct']
    mobileV = vendorData['Mobile']
    telV = vendorData['Tel']
    wcV = vendorData['WC']
    emailV = vendorData['email']

    ins_query('INSERT INTO a_'+category+' (code, url, name, description, price1, price2, price3, img1, img2, img3, img4, vendor) VALUES("'+codeP+'","'+urlP+'","'+nameP+'","'+desP+'","'+price1+'","'+price2+'","'+price3+'", "'+img1+'", "'+img2+'", "'+img3+'", "'+img4+'", "'+contactV+'")')




