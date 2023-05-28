from WorldOfGames.resources.ApplicationGlobals import *


def get_game_selections(games_dictionary):
    games_message = 'Please choose a game to play: \n'
    for game_id in games_dictionary:
        for game in games_dictionary[game_id]:
            games_message = games_message + f'{game_id}. {game}  -  {games_dictionary[game_id][game]} . \n'
    return games_message


def validate_game_difficulty():
    try:
        selection = int(input("please select a game difficulty (0 .. 5) \n"))
    except:
        print('selected value must be number')
        return False
    if selection < 1 or selection > 5:
        print('difficulty out of range')
        return False
    else:
        return selection


def validate_game_selection():
    try:
        selection = int(input("please select a game from list \n"))
    except:
        print('selected value must be number')
        return False
    if available_games.get(selection):
        print(f'selected game : {available_games.get(selection)} \n\n')
        return selection
    else:
        print('selected value not valid')
        return False


def get_welcome_message(name):
    return f'Hello {name} and welcome to the World of Games (WoG). ' \
           f'\nHere you can find many cool games to play.\n\n'


def print_user_selection(input):
    print(input)


def welcome(name):
    print(get_welcome_message(name))
    if load_game():
        print(f' \n  \n user selection summery: \n {user_input} ')



def load_game():
    print(get_game_selections(available_games))
    while not user_input['selected_game']:
        user_input['selected_game'] = validate_game_selection()
    while not user_input['game_difficulty']:
        user_input['game_difficulty'] = validate_game_difficulty()
    return True
