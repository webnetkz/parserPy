import pymysql

#server connection
mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="yiwu"
)


def ins_query(sql):
  mycursor = mydb.cursor() #cursor created
  mycursor.execute(sql)
  mydb.commit()
  mycursor.close()

def get_query(sql):
  mycursor = mydb.cursor()
  mycursor.execute(sql)
  res = mycursor.fetchall()
  return res


