from db import get_query, ins_query
from getLastPage import get_lp, get_products_link

data = get_query('SELECT * FROM cats  ORDER BY id DESC;')

for x in data:

    cat = x[1].lower()

    if get_query('SELECT * FROM information_schema.tables WHERE table_name = "'+cat+'"'):
        print(cat + ' Complete')
        print('-'*30)
    else:
        category = x[2]

        url = 'http://en.yiwugo.com/search/s.html?cpage=1&queryKey='+category
        if get_lp(url):
            lp = get_lp(url) 
        else:
            lp = 1

        ins_query("CREATE TABLE IF NOT EXISTS `"+x[1]+"`(id int(12) AUTO_INCREMENT, link varchar(500), code varchar(50), PRIMARY KEY (id));")
                    
        for o in range(1, lp):
            url = 'http://en.yiwugo.com/search/s.html?cpage='+str(o)+'&queryKey='+category

            allProduct0fPage = get_products_link(url)
            for prod in allProduct0fPage:
                ins_query("INSERT INTO `"+x[1]+"` (link, code) VALUES('"+prod[0]+"', '"+prod[1]+"')")
                print('Append product = ' + prod[1])
                print('-' * 100)


        print('Append category ' + x[1])
        print('-' * 100)



