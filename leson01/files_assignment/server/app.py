

from flask import Flask, request, jsonify
from flask_cors import CORS
from src import files_utils

app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/check-subfolder-files', methods=['POST'])
def execute_module():
    result = files_utils.check_subfolder_files()
    return result

if __name__ == '__main__':
    app.run()