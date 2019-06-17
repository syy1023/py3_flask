from flask import request
from flask import Flask
from flask import render_template
from flask import session

app=Flask(__name__)
@app.route('/login',methods=['POST','GET'])
def login(user=None):
    if request.method=='POST':
        if request.form['user']=='anryan':
            session['user']=request.form['user']
            return 'Anryan login successfully'

        else:
            return 'Sorry %s you are not permitted in' % request.form[user]

    if 'user' in session:
        return 'Welcome back %s' %session['user']

    else:
        title = request.args.get('title', 'friend')
        return render_template('inside_built_object_login.html', title=title)

app.secret_key='12345'




if __name__=='__main__':
    app.run()
