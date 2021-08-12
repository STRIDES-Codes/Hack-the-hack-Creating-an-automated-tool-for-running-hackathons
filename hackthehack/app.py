import os, csv, io
from flask import Flask
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from csv_test import *

UPLOAD_FOLDER = '/home/pi/flaskproject/hackthehack/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "csv"

#def do_stuff(csv_reader):
	


@app.route("/", methods=['GET','POST'])
def hack_the_hack():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			#file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			#return redirect(url_for('hack_the_hack', name=filename))
			stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
			data = csv.reader(stream)
			parse_csv(data)
			#file.close()
	return '''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>'''


