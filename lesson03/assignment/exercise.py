import datetime
import json
import requests
from matches_boy import draw_matches_boy

exercise_file_name = 'server/public/words.txt'


def print_ex_boundary(ex):
    print(f"-----------------------\n {ex}  ==> \n .... ")


def ex_01():
    return " \n " \
           "try: \n" \
           "   a = 1 / 0\n" \
           "   return 'SUCCESS'\n" \
           "except ZeroDivisionError:\n" \
           "   return 'ERROR : illegal division'\n" \
           "except:\n" \
           "   return 'ERROR : unknown error'\n"


def ex_02():
    return "this code is legal - finally will occure even if there is an error. \nin this simple sentence , " \
           "there should be no error"


def ex_03():
    return "any error can be caught here , it is base exception handling"


def ex_04():
    return "when using generic error handling , we dont have granularity \noutputting the real issue to the application"


def ex_05():
    return "a. IOERROR is raised it indicate that there was an issue with file use - either disk space, " \
           "file permission or any other file error was invoked \n" \
           "b. when having ZeroDivisionError , it indicates that we tried to divide by zero, which is wrong"


def create_or_open_file(file_name, mode='a', encoding='utf-8'):
    try:
        file = open(file_name, mode=mode, encoding=encoding)
        return file
    except Exception as e:
        print("failed to open / crete file to write", str(e))
        return None


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
    str = ''
    if file:
        for line in file:
            str = str + line
    return str


def ex_06():
    file = create_or_open_file(exercise_file_name)
    if file :
        update_text_file(file, f'  עידו ביסטרי  {str(datetime.datetime.now())} ')
        close_file(file)
    else:
        print('failed to open file !!! ')


def ex_07():
    file = create_or_open_file(exercise_file_name, mode='r')
    if file:
        print(get_file_content(file))
        close_file(file)
    else:
        print('failed to open file !!! ')


def ex_09_a():
    endpoint1_url = 'http://127.0.0.1:30000/api/v1/file/'
    endpoint1_params = {'dir': './server/public/'}

    response1 = requests.get(endpoint1_url, params=endpoint1_params)
    print(response1.text)


def ex_09_b():
    endpoint_url = 'http://127.0.0.1:30000/api/v1/file/content'
    endpoint_params = {'file': './server/public/words.txt'}

    response = requests.get(endpoint_url, params=endpoint_params)
    print(response.text)


def ex_09_c():
    endpoint_url = 'http://127.0.0.1:30000/api/v1/file/register'
    endpoint_data = {"file": "./server/public/word.txt", "data": "hello"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(endpoint_url, data=json.dumps(endpoint_data), headers=headers)
    print(response.text)


def ex_10():
    draw_matches_boy("green")
    return "matches boy was created in this folder , check file : ./stick_figure_man.png"
