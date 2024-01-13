import pymysql

conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',passwd="root@1234",charset="utf8",db='my_database01')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("insert into tb7(name,password,email,age,salary,ctime) values('wangam','1122','wangam@123','37','888','2024-01-11 21:00')") 
conn.commit()

cursor.close
conn.close
