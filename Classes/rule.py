class FindWinner:
    def __init__(self, player, computer, arr) -> None:
        self.player = int(player)
        self.computer = int(computer)
        self.num_moves = len(arr)

    def find_winner(self):
        half_length = self.num_moves // 2

        player_range = [self.player]
        computer_range = [self.computer]

        for i in range(1, half_length + 1):
            player_range.append((self.player + i) % self.num_moves)
            computer_range.append((self.computer + i) % self.num_moves)

        if self.player == self.computer:
            print("It's a Draw!")
        elif self.computer in player_range:
            print('You Loose :(')
        else:
            print('You win!')


