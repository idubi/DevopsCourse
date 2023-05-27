import requests
import json
from datetime import date

ex_buffer = ' -->       '
ex_sub_buffer = '       '


def ex_1():
    num_1 = int(input(f"{ex_sub_buffer}Please enter 1st number (X):"));
    num_2 = int(input(f"{ex_sub_buffer}Please enter 2nd number:(Y) "));
    print(f'{ex_buffer} ex_1 ==>')
    decision = 'EqUaL'
    if num_1 > num_2:
        decision = "BIG"
    elif num_1 < num_2:
        decision = "small"
    print(f'{ex_sub_buffer}{decision}')


def ex_2():
    print(f'{ex_buffer} ex_2 ==>')
    for i in range(5):
        print(f'{ex_sub_buffer}{i} ')


def ex_3():
    seasons = ['', 'summer', 'winter', 'fall', 'spring']
    print(f'{ex_buffer} ex_3 ==>')
    for i in range(1, 5):
        print(f'{ex_sub_buffer}{"i" * i} = {seasons[i]}')


def ex_4():
    seasons = ['', 'summer', 'winter', 'fall', 'spring']
    print(f'{ex_buffer} ex_4 ==>')
    print(f'{ex_sub_buffer}a. loop will run 10 times\n{ex_sub_buffer}b. 10 will be printed last')


def ex_4():
    print(f'{ex_buffer} ex_4 ==>')
    print(f'{ex_sub_buffer}a. loop will run 10 times\n{ex_sub_buffer}b. 10 will be printed last')


def ex_5():
    def usd_to_ils():
        url = "https://api.apilayer.com/fixer/convert?to=ILS&from=USD&amount=1"

        payload = {}
        headers = {
            "apikey": "9rSd6tFKuqRLEQg8HJ0dyuDd4JdUXoKO"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        json_object = json.loads(response.text)
        return json_object['info']['rate']

    birth_year = 1973
    name = 'ido bistry'
    currency = usd_to_ils()
    is_fly_abroad = True
    addr_appartment_number = 84
    print(f'{ex_buffer} ex_5 ==>')
    age = date.today().year - birth_year
    print(f'{ex_sub_buffer}a. age : {age} ')
    print(f'{ex_sub_buffer}b. first letter of family name : {name.split()[1][0]}')
    print(f'{ex_sub_buffer}c. current currency exchange rate : {currency}')
    print(f'{ex_sub_buffer}e. apartment # : {addr_appartment_number}')
    print(f'{ex_sub_buffer}f. :-)  ')
    print(f'{ex_sub_buffer}g. currency + age = {currency + age}')


def ex_6():
    phone = str(input(f"{ex_sub_buffer}Please enter phone number:"));
    print(f'{ex_buffer} ex_6 ==>')
    print(f'{ex_sub_buffer}phone number:{phone}')


def ex_7():
    print(f'{ex_buffer} ex_7 ==>')

    def print_hello():
        print(f'{ex_sub_buffer}hello')

    def calculate():
        print(f'{ex_sub_buffer}{5 + 3.2}')

    print_hello()
    calculate()


def ex_8():
    print(f'{ex_buffer} ex_8 ==>')

    def get_number():
        return int(input(f"{ex_sub_buffer}Please enter number for division:"));

    def get_name():
        return str(input(f"{ex_sub_buffer}Please enter your name:"));

    print(f'{ex_sub_buffer}{get_number() / 2}')
    print(f'{ex_sub_buffer}{get_name()}')


def ex_9():
    print(f'{ex_buffer} ex_9 ==>')

    def sum_2_numbers():
        num_1 = int(input(f"{ex_sub_buffer}Please enter number for sum:"));
        num_2 = int(input(f"{ex_sub_buffer}Please enter 2ND number for sum:"))
        return num_1 + num_2

    def concat_strings():
        str_1 = str(input(f"{ex_sub_buffer}Please enter a string:"));
        str_2 = str(input(f"{ex_sub_buffer}Please enter 2ND string:"))
        return str_1 + ' ' + str_2

    print(f'{ex_sub_buffer}{sum_2_numbers()}')
    print(f'{ex_sub_buffer}{concat_strings()}')


def ex_10():
    print(f'{ex_buffer} Challenge 10 ==>')
    for i in range(1, 11):
        print(ex_sub_buffer + '#' * i)


def ex_11():
    print(f'{ex_buffer} Challenge 11 ==>')
    def print_x(size) :
        for i in range(0, size):
            line_str = ''
            for j in range(size+1):
                if j == i + 1 or j == size - i:
                    line_str = line_str + '#'
                else:
                    line_str = line_str + ' '
            print(ex_sub_buffer + line_str)
    print_x(7)


def ex_12():
    print(f'{ex_buffer} Challenge 11 ==>')

    def get_num():
        return int(input(f"{ex_sub_buffer}Please enter number for calculation:"))

    def sum_digits(num):
        sum_dig = 0
        for dig_num in str(num):
            sum_dig = sum_dig + int(dig_num)
        return sum_dig

    print(ex_sub_buffer + str(sum_digits(get_num())))
