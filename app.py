import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, Response , send_file)

app = Flask(__name__)


@app.route('/')
def get_octet_stream():
    # Replace this with your octet stream data retrieval logic
    octet_stream_data = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    res = None
    with open('./static/md.ans' , 'r' , encoding = "ISO-8859-1") as file:
        res = file.readlines()

    return Response(res, mimetype='application/octet-stream')

# def index():
#    print('Request for index page received')
#    return render_template('index.html')


@app.route('/logo')
def send_logo():
    # file_path = 'path/to/file.ext'  # Replace with the actual path to your file

    # # Set the appropriate headers for octet stream
    # headers = {
    #     'Content-Disposition': 'attachment; filename=md.ans',
    #     'Content-Type': 'application/octet-stream',
    # }
    # # return send_file(file_path, attachment_filename='md.ans', headers=headers)
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'md.ans', mimetype='application/octet-stream')
    # return send_file()

if __name__ == '__main__':
    app.run()
    