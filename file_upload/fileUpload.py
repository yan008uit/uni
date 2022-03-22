import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template, send_from_directory, url_for
from flask_wtf.csrf import CSRFProtect
import secrets

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'ogg', 'zip'}

csrf = CSRFProtect(app)

@app.route('/')
def form():
    return render_template('upload.html')

@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            basedir = os.path.abspath(os.path.dirname(__file__))
            filename = secure_filename(file.filename)
            file1 = os.path.join(basedir, app.config ['UPLOAD_FOLDER'], filename)
            file.save(file1)
            #send file name as parameter to downlad
            return redirect(url_for('download_file', filename=filename) )

    return render_template('upload.html')


# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)

@app.route('/return-files/<filename>')
def return_files(filename):
    basedir = os.path.abspath(os.path.dirname(__file__))
    absolute_path = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    return send_from_directory( absolute_path, filename, as_attachment=False, attachment_filename='')

app.secret_key = secrets.token_urlsafe(16)

if __name__ == "__main__":
    app.run(debug=True)