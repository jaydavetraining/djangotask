import random

class SnakeAndLadders:
    def __init__(self, players, num_snakes, num_ladders):
        self.board = self.create_board()
        self.players = players
        self.positions = {player: 1 for player in players}#all player staring position 
        self.snakes = {}
        self.ladders = {}
        self.setup_snakes_and_ladders(num_snakes, num_ladders)
    
    def create_board(self):
        board = []
        for i in range(10):
            row = list(range(i * 10 + 1, (i + 1) * 10 + 1))
            if i % 2 == 1:
                row.reverse()
            board.append(row)
        return board

    def setup_snakes_and_ladders(self, num_snakes, num_ladders):
        positions = set()
        
        while len(self.snakes) < num_snakes:
            start = random.randint(11, 99)
            end = random.randint(1, start - 10)
            if start not in positions and end not in positions:
                self.snakes[start] = end
                positions.add(start)
                positions.add(end)

        while len(self.ladders) < num_ladders:
            start = random.randint(1, 90)
            end = random.randint(start + 10, 100)
            if start not in positions and end not in positions:
                self.ladders[start] = end
                positions.add(start)
                positions.add(end)
        print(self.snakes,"+++++++++")
        print(self.ladders,"+++++++++")
    
    def display_board(self):
        print("\nBoard:")
        for row in self.board[::-1]: 
            for cell in row:
                player_here = [player[0] for player in self.players if self.positions[player] == cell]
                if player_here:
                    print(f"{''.join(player_here)}".ljust(4), end=' ')
                elif cell in self.snakes:
                    print(f"S{self.snakes[cell]}".ljust(4), end=' ')
                elif cell in self.ladders:
                    print(f"L{self.ladders[cell]}".ljust(4), end=' ')
                else:
                    print(f"{cell}".ljust(4), end=' ')
            print()
    
    def roll_die(self):
        # return random.randint(1, 6)
        user_input=int(input('enter value in (1,6)'))
        return user_input
    
    def move_player(self, player, move):
        position = self.positions[player]
        new_position = position + move
        
        if new_position > 100:
            new_position = position  
            self.display_board()

     
        new_position = self.snakes.get(new_position, new_position)
        new_position = self.ladders.get(new_position, new_position)

        self.positions[player] = new_position
    
    def check_all_win(self):
        my_player_position=[]
        for value in self.positions:
            my_player_position.append(self.positions[value])
        result = all(i==100  for i in my_player_position)
        if result:
            return True

    def has_winner(self,myplayer):
        for player, position in self.positions.items():
            if player==myplayer:
                if position == 100:
                    return player
        return None
    
    def play(self):
        while True:

            for player in self.players:
                if self.positions[player] == 100:
                    continue
                while True:
                    input(f"{player}'s turn. Press Enter to roll the die...")
                    move = self.roll_die()
                    print(f"{player} rolled a {move}")
                    self.move_player(player, move)
                    self.display_board()
                    winner = self.has_winner(player)
                    if winner:
                        print(f"Congratulations {winner}, you won!")
                        
                    if self.check_all_win():
                        return
                    
                    if move != 6:
                        break

def main():
    players = input("Enter player names (comma separated): ").split(",")
    players = [player.strip() for player in players]
    
    if not 2 <= len(players) <= 4:
        print("You need 2 to 4 players to play.")
        return
    
    try:
        num_snakes = int(input("Enter the number of snakes: "))
        num_ladders = int(input("Enter the number of ladders: "))
    except ValueError:
        print("Please enter valid numbers for snakes and ladders.")
        return

    game = SnakeAndLadders(players, num_snakes, num_ladders)
    game.display_board()  
    game.play()

main()