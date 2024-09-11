from flask import render_template, request, send_file, Blueprint, current_app
from werkzeug.utils import secure_filename
from app.utils.files import merger as mg
import os

upload = Blueprint('upload', __name__)

@upload.route('/')
def upload_page():
    return render_template('upload.html')

@upload.route('/upload_file', methods = ['GET','POST'])
def upload_files():
    try:
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if request.method == 'POST':
            files = request.files.getlist("file")
            
            for file in files:
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_folder, filename))

            pdf_files = [upload_folder + '/' + pdfs for pdfs in os.listdir(upload_folder) if pdfs.endswith(".pdf")]
            user_filename = str(request.form.get('file-name')) + '.pdf'

            path = mg.merger(user_filename, pdf_files)
            
            return send_file(path, as_attachment=True)
    except Exception as err:
        return render_template('error.html', err=err)