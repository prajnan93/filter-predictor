from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename
from auto_filter import AutoFilter
from image_model import ImageModel
from filter_bank import CATEGORIES, FILTER_NAMES

auto_filter = AutoFilter(verbose=True)


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

    filename_wo_ext = os.path.splitext(filename)[0]

    image_model = ImageModel(location)

    # Call classifier to get the category

    category_id = 1

    filter_ranks = auto_filter.get_filter_ranking(category_id=category_id)
    processed_files = []
    for filter_id, filter_configs in filter_ranks:
        processed_configs = []
        for filter_config_id in filter_configs:
            image_model.apply_filter(filter_id=filter_id, config_id=filter_config_id)
            processed_configs.append(image_model.save(filename_wo_ext, 
            filter_id=filter_id, config_id=filter_config_id))
        processed_files.append((FILTER_NAMES[filter_id], processed_configs))

    print(processed_files)

    return render_template("upload.html", nb_faces=2, source=os.path.join(UPLOAD_FOLDER, filename),
     processed_files=processed_files)

if __name__ == "__main__":
    app.run()
