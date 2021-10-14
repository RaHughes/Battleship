class Player:
    def __init__(self, name, fleet, board):
        self.name = name
        self.fleet = fleet
        self.turn = None
        self.board = board
        self.ships_sunk = 0

    def place_ships(self):
        print()
        print(f'It is {self.name}s turn to place their ships.')
        print()
        names = []
        for ship in self.fleet.ships:
            names.append(ship.name.lower())
        while names != []: 
            user_input = input(f'Which ship would you like to place? {names}: ').lower()
            if user_input not in names:
                print(f'Im sorry, {user_input} was not an option. Please try again')
                print()
            for ship in self.fleet.ships:
                if user_input == ship.name.lower():
                    self.board.show_board()
                    print(f'Your {ship.name} is {ship.space_size} spaces long. You must use {ship.space_size} touching tiles to place it.')
                    print()
                    user_location = input(f'Where would you like to place your {ship.name}? Please input {ship.space_size} tiles seperated by a space: ')
                    print()
                    locations = user_location.split()
                    if len(locations) > ship.space_size:
                        print('Im sorry, but you input that incorrectly. Please try again, and follow the prompts more carefully.')
                        print()
                        break
                    for location in locations:
                        ship.location.append(location)
                    print(f'Your {ship.name} has been placed on tiles {locations}')
                    print()
                    names.remove(ship.name.lower())
        print()
        print(f'{self.name} has placed all of his ships!')
        print()
        print()
        print()
        print()                    


    def attack(self, other_player):
        print(f'It is {self.name}s turn to Attack!')
        print(f'Ships Sank: {self.ships_sunk}')
        self.board.show_board()
        user_guess = input('Please input the tile you wish to attack: ')
        did_miss = True
        for ship in other_player.fleet.ships:
            for location in ship.location:
                if user_guess == location:
                    ship.space_size -= 1
                    print()
                    print(f'💥 BOOM 💥! You hit one of {other_player.name}s ships!')
                    print()
                    print()
                    for row in self.board.rows_and_columns:
                        for tile in row:
                            if tile == user_guess:
                                row[row.index(tile)] = '💥'
                                break
                    did_miss = False
                    self.check_fleet(other_player)
                    break
        if did_miss == True:
            print()
            print('💦 SPLASH 💦! You missed!')
            print()
            print()
            for row in self.board.rows_and_columns:
                for tile in row:
                    if tile == user_guess:
                        row[row.index(tile)] = '💦'
            self.check_fleet(other_player)        


    def check_fleet(self, other_player):
        for ship in other_player.fleet.ships:
            if ship.space_size == 0:
                other_player.fleet.ships.remove(ship)
                self.ships_sunk += 1                