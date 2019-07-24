


import pymysql
from flask import Flask

app=Flask(__name__)

user=input("请输入用户名")
pwd=input("请输入密码")

conn=pymysql.connect(host="127.0.0.1",port=3306,user='root',password='12345',db='testdb',charset='utf8')

cursor=conn.cursor()

sql="select * from userinfo where username='%s' and pwd='%s' " %(user,pwd)

print(sql)

cursor.execute(sql)

result=cursor.execute(sql)

print(result)


cursor.close()
conn.close()


if result:
    print('登录成功')
else:
    print('登录失败')

if __name__=='__main__':
    app.run()