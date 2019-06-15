from flask import request
from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        if request.form['user']=='anryan':
            return 'Anryan login successfully'

        else:
            return 'Sorry you are not permitted in'

    title=request.args.get('title','friend')
    return render_template('inside_built_object_login.html',title=title)



if __name__=='__main__':
    app.run()





