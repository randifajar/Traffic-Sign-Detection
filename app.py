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
app.config['UPLOADED_FILES_DEST'] = 'E:/Tugas/Semester 8/Tugas Akhir/GUI/TS Detection/ScaledYOLOv4/uploads'
app.config['INFERENCED_FILES_DEST'] = 'E:/Tugas/Semester 8/Tugas Akhir/GUI/TS Detection/ScaledYOLOv4/inference/output'

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
        # source1 = url_for('get_source', filename=filename)
        # source = "E:/Tugas/Semester 8/Tugas Akhir/GUI/TS Detection/ScaledYOLOv4" + source1
        # print(source)
        # cobacok.main_detect(weights, source, img_size, conf_thres, iou_thres)
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


@app.route('/detect_image/<filename>', methods=['GET', 'POST'])
def detect_file(filename):
    source1 = url_for('get_source', filename=filename)
    source = "E:/Tugas/Semester 8/Tugas Akhir/GUI/TS Detection/ScaledYOLOv4" + source1
    print("source ", source)
    yolo_detect.main_detect(weights, source, img_size, conf_thres, iou_thres)
    detect_file_url = url_for('get_file', filename=filename)
    print("detect_file_url ", detect_file_url)
    return render_template('detect_image.html', detect_file_url=detect_file_url)


@app.route('/detect_video/<filename>', methods=['GET', 'POST'])
def detect_video(filename):
    source1 = url_for('get_source', filename=filename)
    source = "E:/Tugas/Semester 8/Tugas Akhir/GUI/TS Detection/ScaledYOLOv4" + source1
    print("source ", source)
    yolo_detect.main_detect(weights, source, img_size, conf_thres, iou_thres)
    detect_video_url = url_for('get_file', filename=filename)
    print("detect_video_url ", detect_video_url)
    return render_template('detect_video.html', detect_video_url=detect_video_url)


@app.route('/', methods=['GET', 'POST'])
def main_menu():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
