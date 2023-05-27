from num2words import num2words

def is_number_divider_without_extra(number,divider):
    return number % divider ==0
def is_divider_contained_in_number(number,divider):
    str_divider = f'{divider}'
    str_number = f'{number}'
    return str_divider in str_number

def print_is_boom (number,divider)  :
    if is_divider_contained_in_number(number,divider) or is_number_divider_without_extra(number,divider):
        print( '======== \n BOOM \n =======' )
    else:
        print(number)

def number_boom (fromNumber,toNumber,divider) :
    for num in  range (fromNumber,toNumber,1):
        print_is_boom(num,divider)

number_names= ["zero", "one", "two","three","four","five"]
def print_number_name (num):
    try:
        print(f'{number_names[num]}')
    except:
        print(f'number not supported , ({num})')

def print_num_in_word (num):
   print(f'{num2words(num,False,"en")}')


number_boom(0,89,7)
#print_number_name(3)
#print_num_in_word(456)

