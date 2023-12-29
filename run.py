from random import randint
import time
import random

# computer and player scores set to 0 
scores = {"computer":0, "player":0}
# Global variables for grid
player_grid_rows = 5
player_grid_column = 10
cpu_grid_rows = 5
cpu_grid_column = 10
#global name variable 
name = ()


class Player_Input:
    def __init__(self, player_name=None,):
        if not player_name:
            player_name = self.get_player_name()

        self.player_name = player_name