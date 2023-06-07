from flask import Blueprint, request, jsonify
from lesson03.assignment.server.services.file_service import *

# Create a Blueprint instance
main = Blueprint('main', __name__)

file_name = 'words.txt'
file_path = './server/public'


def is_error_response(message):
    return message.startswith('[Errno')


@main.route('/')
def file_list():
    path = request.args.get('dir') or file_path
    files = list_files(path)
    if isinstance(files, str):
        response_date = {
            'success': False,
            'status': 500,
            'message': files
        }
    else:
        response_date = {
            'success': True,
            'status': 200,
            'files': files
        }
    return jsonify(response_date), response_date.get('status')


@main.route('/content', methods=['GET'])
def get_file_content():
    path = request.args.get('file') or file_path + '/' + file_name
    content = file_content(path)

    if not is_error_response(content):
        response_date = {
            'success': True,
            'status': 200,
            'content': content
        }
    else:
        response_date = {
            'success': False,
            'status': 500,
            'message': content
        }
    return jsonify(response_date), response_date.get('status')


@main.route('/register', methods=['POST'])
def register():
    path = (request.get_json().get('file') or file_path + '/' + file_name)
    data = (request.get_json().get('data') or 'hello')
    write_result = write_content(path, data)

    if isinstance(write_result, bool) and write_result:
        content = file_content(path)
        response_date = {
            'success': True,
            'status': 201,
            'content': content
        }
    else:
        response_date = {
            'success': False,
            'status': 501,
            'message': write_result
        }
    return jsonify(response_date), response_date.get('status')
