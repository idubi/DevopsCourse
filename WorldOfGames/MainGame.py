from Live import welcome
from resources.ApplicationGlobals import user_input

user_input['user_name'] = str(input('please enter your name \n'))
welcome(user_input['user_name'])
