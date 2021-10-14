from player import Player
from fleet import Fleet
from board import Board


user_one = input('Player One, insert your name: ')
user_two = input('Player Two, insert your name: ')
player_one = Player(user_one, Fleet(), Board())
player_two = Player(user_two, Fleet(), Board())
player_one.fleet.create_fleet()
player_two.fleet.create_fleet()
    



player_one.place_ships()
player_two.place_ships()

print(f'Let the game of Battleship Commence! {player_one.name} vs {player_two.name}!')
print()

while player_one.fleet.ships != [] or player_two.fleet.ships != []:
    player_one.attack(player_two)
    if player_two.fleet.ships == []:
        print(f'{player_one.name} is the winner!')
        break
    player_two.attack(player_one)
    if player_one.fleet.ships == []:
        print(f'{player_two.name} is the winner!')
        break
   
