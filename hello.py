#coding=utf-8
from flask import Flask
from flask import request
app = Flask(__name__)
'首先引入了Flask包，并创建一个Web应用的实例”app”'
'这个函数级别的注解指明了当地址是根路径时，就调用下面的函数MVC中controller'

@app.route('/')
def index():
    return '<header><br>hello python</br></header>'

'当请求的地址符合路由规则时，就会进入该函数。MVC中的model'


'在url中定义参数,字符串参数'
@app.route('/hi/<name>')
def hello(name):
    return "<h3>hi,%s</h3>"%name


'在url中定义参数,整数参数'

@app.route('/hello/<int:user_id>')
def greet(user_id):
    return "<h2>say greeting from %d number member</h2>" %user_id

'多路由的url'
@app.route('/num')
@app.route('/num/<int:number>')
@app.route('/num/<float:number>')
def Num(number=None):
    if (str(number)).isdigit():
        return "<h4>say a number %d</h4>" % number
    else:
        return "No number"

'不同的请求如post，delete，patch，put'
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        return '<h3>this is a post request<h3>'
    else:
        return "<h3>this is a GET request </h3>"





if __name__=='__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)


    '上述是制定访问的host和端口，或者app.run()，访问http://127.0.0.1:5000/'
