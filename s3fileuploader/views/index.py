from flask import Blueprint, render_template, flash, redirect, url_for

index = Blueprint("index", __name__)
index_path = 'index.serve_index'


@index.route('/', methods=["GET"])
def serve_index():
    return render_template('upload.html', files=[])


@index.route('/uploads', methods=["POST"])
def upload_file():
    flash('File successfully uploaded')
    return redirect(url_for(index_path))


@index.route('/uploads/<filename>', methods=['GET'])
def download_file(_):
    return redirect(url_for(index_path))


@index.route('/uploads/<filename>', methods=['DELETE'])
def delete_file(_):
    return redirect(url_for(index_path))
