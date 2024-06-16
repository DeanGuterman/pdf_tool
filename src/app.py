from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
import atexit
from splitter import split_pdf
from merger import merge_pdfs
from utils import delete_folders, clear_folder

"""
Flask application for PDF processing
"""

app = Flask(__name__, template_folder='../templates')

# Define upload and output folders
UPLOAD_FOLDER = '../uploads'
OUTPUT_FOLDER = '../output'

# Create upload and output folders if they don't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


# The main page of the webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if and what kind of form submit is it
    if request.method == 'POST':
        print(request.form)

        for file in request.files.getlist('split_file') or request.files.getlist('merge_files'):
            if file:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)

        # If it's a pdf splitting form
        if 'split' in request.form:
            print("Split form submitted")
            split_pdf(UPLOAD_FOLDER, OUTPUT_FOLDER)

        # If it's a pdf merging form
        elif 'merge' in request.form:
            print("Merge form submitted")
            merge_pdfs(UPLOAD_FOLDER, OUTPUT_FOLDER)

        return redirect(url_for('index', files=os.listdir(OUTPUT_FOLDER)))

    return render_template('index.html', files=os.listdir(OUTPUT_FOLDER))


# Route for sending the processed files to the user
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


# Delete the created folders, lambda is needed because atexit.register expects a function
atexit.register(lambda: delete_folders([UPLOAD_FOLDER, OUTPUT_FOLDER]))


if __name__ == '__main__':
    app.run(debug=True)