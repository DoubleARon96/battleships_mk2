from random import randint
import time
import random

# computer and player scores set to 0
scores = {"computer": 0, "player": 0}
# Global variables for grid
player_grid_rows = 5
player_grid_column = 10
cpu_grid_rows = 5
cpu_grid_column = 10
# global name variable
name = ()


class Player_Input:
    """
    this creates a checker and the player input so it will always check what 
    is inputted 
    """
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
    # this function makes an exception for player inputs

    def get_player_choice(self):
        valid_input = False
        while not valid_input:
            print("Input Guild:first number is Y axis (0 To 4) e.g: 0,4")
            print("Input Guild:second number is X axis (0 To 9) eg: 0,9")
            player_input = input("Enter your choice: ")
            try:
                player_choice = list(map(int, player_input.split(",")))
                if (len(player_choice) != 2):
                    raise Exception("To Many Inputs")

                elif (
                    player_choice[0] not in range(5) or
                    player_choice[1] not in range(10)
                ):

                    raise Exception("Input Out of Range")
                valid_input = True

            except (ValueError, Exception) as e:
                e = "Please refer to the example for inputs = e.g: 0,0"
                print(e)
                valid_input = False

        return player_choice


class Battleship():

    """
    this class is the battle ship
    and gives it the states it needs
    to change from alive with a boolean
    """
    def __init__(self, coords_X, coords_Y):
        self.coords_X = coords_X
        self.coords_Y = coords_Y
        self.Is_Alive = True

    def set_random_location(self):
        random_nums_Y = [0, 1, 2, 3, 4]
        random_num_choice_Y = random.choice(random_nums_Y)
        random_nums_X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random_num_choice_X = random.choice(random_nums_X)
        self.coords_X = random_num_choice_X
        self.coords_Y = random_num_choice_Y

    def check_hit_or_miss(self, X, Y):

        if (X == self.coords_X and Y == self.coords_Y):
            self.Is_Alive = False
            return "Hit!"

        else:
            return "Miss!"


class grid_drawing():

    grid = [[], []]
    """
    this class draws out the grid and updates the ships, hits, misses
    """
    def __init__(self, ships, misses):
        y = 5
        x = 10
        self.grid = [["O" for _ in range(x)] for _ in range(y)]
        for ship in ships:
            # this if statement checks if the ship is
            # a S or if its been hit
            if (ship.Is_Alive):
                self.grid[ship.coords_Y][ship.coords_X] = "S"
            else:
                self.grid[ship.coords_Y][ship.coords_X] = "H"
        for i, j in misses:
            self.grid[i][j] = "M"
            self.ships = ships
            self.misses = misses

    def update_grid(self, ships, misses):
        for ship in ships:

            if (ship.Is_Alive):
                self.grid[ship.coords_Y][ship.coords_X] = "S"
            else:
                self.grid[ship.coords_Y][ship.coords_X] = "H"
        for i, j in misses:
            self.grid[i][j] = "M"

    def print_grid(self):
        print("----------------------")
        print("|      0123456789    |")
        for i in range(len(self.grid)):
            print("|    " + str(i) + " ", end="")
            for j in range(len(self.grid[i])):
                # This code will hide the ships and empty spaces
                # So you can easily hide the grid
                if (self.grid[i][j] == "S" or self.grid[i][j] == "O"):
                    print("?", end="")
                else:
                    print(self.grid[i][j], end="")
            print("    |")
        print("----------------------")


'\n'


class Player_Input_checks():
    """
    this is another input checker and makes sure 
    the length and the numbers and letter will be excepted
    """

    def __init__(self, player_choice, misses, hits):

        self.player_choice = player_choice
        self.misses = misses
        self.hits = hits

    def check_input(self, input):
        if len(input) == 2:
            if input[0].isalpha() and input[0].upper() in "ABCDE":
                if input[1].isnumeric() and int(input[1]) in range(0, 11):
                    if input in ships:
                        return True

        return False


class Game:
    """
    this function is the main one and make it run
    it makes the game have a set amount of rounds
    and sets score too
    """

    def __init__(self, shots, score):
        self.shots = shots
        self.score = score

    def start(self):
        ship1 = Battleship(0, 0)
        ship1.set_random_location()

        ship2 = Battleship(0, 0)
        ship2.set_random_location()

        ship3 = Battleship(0, 0)
        ship3.set_random_location()

        ships = [ship1, ship2, ship3]

        misses = []

        self.shots = 10

        player = Player_Input()

        player.check_player_name()

        gd = grid_drawing(ships, misses)
        print("Shots left: " + str(self.shots))
        gd.print_grid()

        game_over = False

        while self.shots > 0 and not game_over:
            player_choice = player.get_player_choice()
            self.shots -= 1
            print(player_choice)

            num_misses = 0
            for ship in ships:
                result = ship.check_hit_or_miss(player_choice[0],
                                                player_choice[1])
                if (result == "Miss!"):
                    num_misses += 1
                else:
                    print(result)

            print("Misses:", len(misses))

            if (num_misses == len(ships)):
                misses.append((player_choice[0], player_choice[1]))

            gd.update_grid(ships, misses)
            print("Shots left: " + str(self.shots))
            gd.print_grid()
            # checks if game over
            if self.shots == 0 or all(not ship.Is_Alive for ship in ships):
                game_over = True
                self.score = self.shots * 10

                if self.shots == 0:
                    print("Game Over! You Ran Out! You lose!")

                else:
                    print("WOOO HOOO You Won This Battle")
                    print(f"Your score is {self.score}")
            # this makes the game reset or end
            while game_over is True:
                answer = input("Do you want to play again? Y to continue")
                if answer.upper() == "Y":
                    game.start()
                else:
                    print("Thanks for playing")
                    break


game = Game(10, 0)
game.start()
