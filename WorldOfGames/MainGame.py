from WorldOfGames.Live import welcome
from WorldOfGames.resources.ApplicationGlobals import user_input

user_input['user_name'] = str(input('please enter your name \n'))
welcome(user_input['user_name'])
