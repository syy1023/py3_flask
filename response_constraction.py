

from flask import Flask,session,request,make_response,render_template

app=Flask(__name__)
@app.route('/login',methods=['POST','GET'])

def login():
    if request.method=="POST":
        if request.form['user']=='anryan':
            session['user'] =request.form['user']
            return 'Welcome, anryan'
        else:
            return "Sorry,%s you are not permitted in" %request.form['user']

    if 'user' in session:
        return 'Glad you come back, %s' %session['user']

    else:
        title=request.args.get('title','Default')
        response=make_response(render_template('inside_built_object_login.html',title=title),200)
        response.headers['key']='value'
        return response
app.secret_key='12345'

if __name__=='__main__':
    app.run()