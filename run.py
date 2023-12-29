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


    def get_player_name(self):
        player_name = ""
        
        while not player_name:
            
            player_name = input("Enter Name Here ").strip()

            if not player_name:

                print("Name Is Required")

    
        print(f"Output:Welcome to the battle {player_name}")
        
        self.player_name = player_name
        return self.player_name
    
    def check_player_name(self):
        """
        checks players name
        """
        if not self.player_name:
            print("please Enter Name")
            self.player_name = self.get_player_name()
    
    def get_player_choice(self):
        valid_input = False
        while not valid_input:
            print("Input Guild:first number is Y axis (0 To 4) and second number is X axis (0 To 9")
            player_input = input("Enter your choice: ")
            try:
                player_choice = list(map(int, player_input.split(",")))
                if(len(player_choice) != 2 ):
                    raise Exception("To Many Inputs")
                valid_input = True
            except Exception as e: 
                print(e)
                valid_input = False
        
        return player_choice