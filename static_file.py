
from flask import Flask

from flask import url_for

app=Flask(__name__)

@app.route('/path')
def index():
    return url_for('static',filename='style.css')


if __name__=='__main__':
    app.run('host=0.0.0.0',debug=True)