from .help import Help
from .rule import FindWinner
import time

class Game:
    def __init__(self,key,turns,comp,hashkey,game) -> None:
        self.pressed_key = key
        self.availabe_turns = turns
        self.computer_turn = comp
        self.hmac_key = hashkey
        self.game_Status = game

    def start_game(self):
        if self.pressed_key in ('1', '2', '3', '4', '5','6','7','0','?'):
            player_turn = self.pressed_key

            if player_turn == '?':
                help_instance = Help(self.availabe_turns)
                help_instance.generate_table()
            elif player_turn == '0':
                print('Goodbye')
                self.game_Status = False
            
            for turn in self.availabe_turns:
                if player_turn == turn['key']:
                    print(f'Your turn: {turn["value"]} \nComputers turn: {self.computer_turn["value"]}')
            
                    instance = FindWinner(turn['key'],self.computer_turn['key'],self.availabe_turns)
                    time.sleep(1)
                    instance.find_winner()
                    time.sleep(1)
                    print(f'HMAC KEY: {self.hmac_key}')           
        else:
            print('Invalid key pressed, try again')
        
    def gameplay(self):
        return self.game_Status