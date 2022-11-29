from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename

app_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=os.path.join(app_dir, 'static'))
app._static_folder = 'static'
UPLOAD_FOLDER = 'static/uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# url_for('static', filename='styles/style.css')

print(os.path.join(app_dir, 'static'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(app_dir, 'static/uploaded/')
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = secure_filename(file.filename)
    location = target + filename
    file.save(location)
    return render_template("upload.html", nb_faces=2, source=os.path.join(UPLOAD_FOLDER, filename),
     filter_cats={'Vivid':[1,2,3], 'Monochrome':[1,2,3], 'Dramatic':[1,2,3]})

if __name__ == "__main__":
    app.run()
