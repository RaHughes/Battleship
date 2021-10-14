from battleship import Battleship
from destroyer import Destroyer
from submarine import Submarine
from aircraft_carrier import AircraftCarrier

class Fleet:
    def __init__(self):
        self.ships = []

    def create_fleet(self):
        self.ships.append(Submarine())
        self.ships.append(Destroyer())
        self.ships.append(Battleship())
        self.ships.append(AircraftCarrier()) 