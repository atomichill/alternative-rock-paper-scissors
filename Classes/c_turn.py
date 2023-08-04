import random

class Computer:
    def __init__(self , array):
        self.passed_array = array

    def computer_move(self) -> str:
        
        moves = []
        for element in self.passed_array:
            moves.append(element)
        
        move = random.choice(moves)
        
        return move
    