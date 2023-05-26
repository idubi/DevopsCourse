#check_subfolder_files.py

from flask import Flask, request, jsonify
import os
import re

def check_file_pattern(pattern,fileName):
    regex = re.compile(pattern)
    match = re.search(regex, fileName)
    if match:
        return True
    else:
        return False


def check_subfolder_files():
    path = request.json.get('path')
    file_pattern = request.json.get('file_pattern')

    if not path:
        return jsonify({'error': 'Path parameter is required.'}), 400

    if not file_pattern:
        return jsonify({'error': 'File pattern parameter is required.'}), 400

    if not os.path.exists(path):
        return jsonify({'error': f"Path '{path}' does not exist."}), 404

    if os.path.isfile(path):
        return jsonify({'error': f"Path '{path}' is a file, not a directory."}), 400

    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    found_file = False
    response_data = []

    for subfolder in subfolders:
        files = [f.name for f in os.scandir(subfolder) if f.is_file() and check_file_pattern(file_pattern,f.name) ]
        if files:
            found_file = True
            response_data.append({
                'subfolder': subfolder,
                'files': files
            })

    if not found_file:
        return jsonify({'message': f"No file matching pattern '{file_pattern}' was found in the requested path."}), 200

    
    
    return jsonify(response_data), 200