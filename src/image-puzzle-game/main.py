from puzzle import Puzzle
from time import sleep


def play():
    """Start the main game sequence"""

    # Welcome the user to the game
    # create animated text effect using time.sleep() define as helper function
    print("Welcome to the puzzle Game!")

    # Instantiate puzzle and display to user
    game = Puzzle("https://imageupload.io/ib/mU2ho0sgtobbOP2_1696886540.jpg")
    game.render_puzzle()
    player_won = False
    sleep(1)


    while not player_won:
        # Ask user which tile they would like to move and to what destination
        user_tile = input("What tile would you like to move?\n")
        user_destination = input("Where would you like to move it to\n")

        # move tile and update empty slot and movable tiles
        moved = game.move(int(user_tile), int(user_destination))
        if not moved:
            print("Choose a valid tile!\n")
        else:
            game.render_puzzle()

        # check if player won
        player_won = game.check_if_player_won()

    game.start_win_sequence()
