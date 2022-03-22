import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template, send_from_directory, url_for, make_response
from flask_wtf.csrf import CSRFProtect
import secrets
from filearchive import FileArchive
from datetime import datetime
from attachment import Attachment

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'ogg', 'zip'}

csrf = CSRFProtect(app)

@app.route('/')
@app.route('/index')
def show_all_files():
    with FileArchive() as db:
        result = db.getAll()
        attachments = [Attachment(*x) for x in result]
        return render_template('upload.html', attachments=attachments)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return redirect(url_for('show_all_files', _external=True))
    file = request.files['file']
    mimetype = file.mimetype
    blob = request.files['file'].read()
    size = len(blob)

    if file.filename == '':
        print('no filename')
        return redirect(request.url)
    elif file and allowed_file(file.filename):
        dateTime = datetime.now()
        filename = secure_filename(file.filename)
        attachment = (size, dateTime, mimetype, filename, blob)
        with FileArchive() as db:
            result = db.add(attachment)
        return redirect(url_for('show_all_files', _external=True))
    else:
        return redirect(url_for('show_all_files', _external=True))

@app.route('/download/<id>')
def download_file(id):
    with FileArchive() as db:
        attachment = Attachment(*db.get(id))
    if attachment is None:
            pass
    else:
        response = make_response(attachment.code)
        response.headers.set('Content-Type', attachment.mimetype)
        response.headers.set('Content-Length', attachment.size)
        response.headers.set(
        'Content-Disposition', 'inline', filename = attachment.filename)
        return response

app.secret_key = secrets.token_urlsafe(16)

if __name__ == "__main__":
    app.run(debug=True)