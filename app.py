from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import yolo_detect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'apahayo'
app.config['UPLOADED_FILES_DEST'] = '/content/TA/uploads'
app.config['INFERENCED_FILES_DEST'] = '/content/TA/inference/output'

run_with_ngrok(app)

weights = './weights/yolov4-csp.pt'
img_size = 416
conf_thres = 0.4
iou_thres = 0.5

photos = UploadSet('files', IMAGES)
videos = UploadSet('files', 'mp4')
configure_uploads(app, (photos, videos))


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only photos are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')


class UploadVideoForm(FlaskForm):
    video = FileField(
        validators=[
            FileAllowed(videos, 'Only vidoes are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')


@app.route('/uploads/<filename>')
def get_source(filename):
    return send_from_directory(app.config['UPLOADED_FILES_DEST'], filename)


@app.route('/inference/output/<filename>')
def get_file(filename):
    return send_from_directory(app.config['INFERENCED_FILES_DEST'], filename)


@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_source', filename=filename)
        print("filename ", filename)
        print("file_url ", file_url)
    else:
        filename = None
        file_url = None
    return render_template('image.html', form=form, file_url=file_url, filename=filename)


@app.route('/video', methods=['GET', 'POST'])
def upload_video():
    form = UploadVideoForm()
    if form.validate_on_submit():
        filename = videos.save(form.video.data)
        file_url = url_for('get_source', filename=filename)
        print("filename ", filename)
        print("file_url ", file_url)
    else:
        filename = None
        file_url = None
    return render_template('video.html', form=form, file_url=file_url, filename=filename)


@app.route('/demo_image')
def demo_image():
    return render_template('demo_image.html')


@app.route('/demo_video')
def demo_video():
    return render_template('demo_video.html')
    

@app.route('/detect_image/<filename>', methods=['GET', 'POST'])
def detect_file(filename):
    source1 = url_for('get_source', filename=filename)
    source = "/content/TA" + source1
    print("source ", source)
    yolo_detect.main_detect(weights, source, img_size, conf_thres, iou_thres)
    detect_file_url = url_for('get_file', filename=filename)
    print("detect_file_url ", detect_file_url)
    return render_template('detect_image.html', detect_file_url=detect_file_url)


@app.route('/detect_video/<filename>', methods=['GET', 'POST'])
def detect_video(filename):
    source0 = "/content/TA"
    source1 = url_for('get_source', filename=filename)
    source_detection = source0 + source1
    print("source_detection ", source_detection)
    yolo_detect.main_detect(weights, source_detection, img_size, conf_thres, iou_thres)
    source2 = url_for('get_file', filename=filename)
    source_convert = source0 + source2
    print("source_convert ", source_convert)
    subprocess.run(["ffmpeg","-i",source_convert,"/content/TA/inference/output/output.mp4"])
    return render_template('detect_video.html', detect_video_url="/inference/output/output.mp4")


@app.route('/', methods=['GET', 'POST'])
def main_menu():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
