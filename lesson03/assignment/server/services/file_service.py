import os


def create_or_open_file(file_name, mode='a', encoding='utf-8'):
    try:
        file = open(file_name, mode=mode, encoding=encoding)
        return file
    except Exception as e:
        print("failed to open / crete file to write", str(e))
        return str(e)


def update_text_file(file, data):
    if file:
        try:
            file.write(data + '\n')
            return True
        except IOError as e:
            print('failed to write to file', e)
            return False
    return False


def close_file(file):
    if file:
        try:
            file.close()
            return True
        except IOError as e:
            print('failed to close hte file', e)
            return False
    return False


def get_file_content(file):
    line_str = ''
    if file:
        for line in file:
            line_str = line_str + line
    return line_str


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


# def get_line(file_path, line_number):
#     file_content = create_or_open_file(file_path, mode='r')
#     res = ''
#     if not isinstance(file_content, str):
#         file_size = len(file_content)
#         if file_size < line_number:
#             print('file size is less then requested line')
#             res = ''
#         else:
#             res = file_content[line_number - 1]
#     close_file(file_content)
#     return res
#
#
# def is_file_empty(file_path):
#     file = create_or_open_file(file_path, mode='r')
#     if not isinstance(file, str):
#         file_size = len(file)
#         return file_size > 0
#     return True
