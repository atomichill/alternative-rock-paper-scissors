import sys
import time
from Classes.hmac import Hmac
from Classes.c_turn import Computer
from Classes.game import Game
from Classes.key import Key
from Classes.chek_args import ChekArguments
 

game_arguments = sys.argv
game_arguments.pop(0)

arguments_instance = ChekArguments(game_arguments)
validation = arguments_instance.is_valid_array()


if validation:
    gameplay = True
    availabe_turns = []
    
    for i in range(len(game_arguments)):
        availabe_turns.append({'key':f'{i + 1}','value': game_arguments[i].capitalize()})
        
    while gameplay:
        key_instance = Key(32)
        game_key = key_instance.generate_key()
        computer_instance =Computer(availabe_turns)
        computer_turn = computer_instance.computer_move() 
        hmac_instance = Hmac(game_key,computer_turn['value'])
        hmac = hmac_instance.calc_hmac()

        print('HMAC:', hmac)
        time.sleep(1)
        print('Available moves: \n')

        for element in availabe_turns:
            print(f'{element["key"]} - {element["value"]}')

        print('\n0 - Exit \n? - Help')

        pressed_key = input('Enter your move: ')
        
        time.sleep(1)
        game_origin = Game(pressed_key,availabe_turns,computer_turn,game_key,gameplay)
        game_origin.start_game()
        time.sleep(3)
        gameplay= game_origin.gameplay()




