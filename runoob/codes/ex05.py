# -*- coding : utf-8 -*-

import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "mydb")
cursor = db.cursor()     #获得操作游标
sql = "select * from employee"
cursor.execute(sql)
data = cursor.fetchall()
print data
db.close()
