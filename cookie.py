
from flask import Flask,render_template,session,make_response,request
import time

app=Flask(__name__)
@app.route('/login',methods=["POST","GET"])
def login():
    response=None
    if request.method=="POST":
        if request.form['user']=='anryan':
            session['user']=request.form['user']
            response = make_response("anryan login successfully")
            response.set_cookie('login_time',time.strftime('%Y-%m-%d %H:%M:%S'))


            #return "welcome %s" %request.form['user']
        else:
            return 'Sorry,%s you are not permitted in' %request.form['user']
    else :
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hi %s you loggin on %s' %(session['user'],login_time))
            # return 'Welcome back %s' %session['user']
        else:
            title = request.args.get('title', 'Friend')
            return render_template('inside_built_object_login.html', title=title)

    return response

app.secret_key='123456'



if __name__=='__main__':
    app.run()