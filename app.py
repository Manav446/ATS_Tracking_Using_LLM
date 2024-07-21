import sys
import warnings
import os

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from src.helper import Helper
from src import constants
from src.logger import logging
from src.exception import CustomException

warnings.filterwarnings("ignore")
app = Flask(__name__)
logger = logging.getLogger("App")

helper = Helper()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['pdf_file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    

    if file:
        filename = secure_filename(file.filename)
        if not os.path.isdir(constants.PDF_TEMP_PATH):
            os.mkdir(constants.PDF_TEMP_PATH)
        filePath = os.path.join(constants.PDF_TEMP_PATH, filename)
        file.save(filePath)
            

    description = request.form.get('description')
    if not description:
        return jsonify({'error': 'No description provided'}), 400

    # Process the file and description here
    prompt_input_variables = {
        "resume_content": helper.resume_data(input_file=filePath),
        "job_description": description
    }

    llm_response = helper.get_response_from_gemini(input_variables=prompt_input_variables)

    return jsonify(llm_response["text"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

