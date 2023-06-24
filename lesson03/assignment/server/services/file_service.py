import os

from lesson03.assignment.exercise import *


def list_files(dir):
    try:
        file_list = os.listdir(dir)
        return file_list
    except IOError as e:
        print('failed to list files in directory ', e)
        return str(e)


def file_content(file_path):
    file = create_or_open_file(file_path, mode='r')
    if not isinstance(file, str):
        content = get_file_content(file)
        close_file(file)
        return content
    else:
        return file


def write_content(file_path, data):
    file = create_or_open_file(file_path)
    if not isinstance(file, str):
        update_text_file(file, data)
        close_file(file)
        return True
    else:
        return file


def get_line(file_path, line_number):
    file = create_or_open_file(file_path, mode='r')
    res = ''
    if not isinstance(file, str):
        file_size = len(file)
        if file_size < line_number:
            print('file size is less then requested line')
            res = ''
        else:
            res = file[line_number - 1]
    close_file(file)
    return res


def is_file_empty(file_path):
    file = create_or_open_file(file_path, mode='r')
    if not isinstance(file, str):
        file_size = len(file)
        return file_size > 0
    return True
