import datetime
import requests

print(datetime.date.today())


def save_name(file_name, name):
    f = open(file_name, 'a',)
    f.write(name + '\n')
    f.close()


def print_file(file_name):
    f = open(file_name)
    for line in f:
        print(line, end='')


def div(x, y):
    try:
        print(int(x / y))
    except ZeroDivisionError:
        print('cant divide by 0')
    except TypeError:
        print('cant divide with string')
        # raise 'pukiDafuki'
    except BaseException:
        print('there was an error on division')


file_name = 'names.txt'

# save_name(file_name, 'doron')
# save_name(file_name, 'yuval')
# save_name(file_name, 'sharon')
# print_file(file_name)

div(9, 3)
div(9, 0)
div(5, '5')

# pip install -r requirements.txt
