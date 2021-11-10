from getLastPage import get_lp, get_products_link
from db import get_query, ins_query

data = get_query('SELECT * FROM cats  ORDER BY id DESC;')

i = 50

def goParse(i, data):
    if(i == 100):
        print('One')
        exit()
    cat = data[i][2]


    url = 'http://en.yiwugo.com/search/s.html?cpage=1&queryKey='+cat
    lp = get_lp(url)
    if lp == '':
        lp = 1

    print(data[1])
    print(data[99])
    print(data[39])
    exit()

    ins_query("CREATE TABLE IF NOT EXISTS `"+data[i][1]+"`(id int(12) AUTO_INCREMENT, link varchar(500), code varchar(50), PRIMARY KEY (id));")
            
    for o in range(1, lp):
        url = 'http://en.yiwugo.com/search/s.html?cpage='+str(o)+'&queryKey='+cat

        allProduct0fPage = get_products_link(url)
        for prod in allProduct0fPage:
            ins_query("INSERT INTO `"+data[i][1]+"` (link, code) VALUES('"+prod[0]+"', '"+prod[1]+"')")
            print('Append product = ' + prod[1])
            print('-' * 100)


    print('Append category ' + data[i][1])
    print('-' * 100)

    i = i + 1
    goParse(i, data)

goParse(i, data)
    





