import os
from flask import Flask,request,redirect,url_for
from werkzeug import secure_filename

UPLOAD_FOLDER='/Users/yuanyuan.shao/Documents/flask/venv/file'
ALLOWED_EXTENSIONS=set(['txt','pdf','png'])
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH']=16*1024*1024


def allowed_file(filename):
    return '.' in filename and  \
            filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__=="__main__":
    app.run(host='0.0.0.0',port='8889',debug=True)


'''
UPLOAD_FOLDER 是上传文件要储存的目录，ALLOWED_EXTENSIONS 是允许 上传的文件扩展名的集合

'''