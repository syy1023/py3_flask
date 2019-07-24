
from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
@app.route('/sayhello/<location>')
@app.route('/sayhi/<name>')
def index(name=None,location=None):
    return render_template('hello.html',name=name,location=location)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)

