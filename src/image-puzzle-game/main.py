from puzzle import Puzzle


def play():
    """Start the main game sequence"""

    # Welcome the user to the game
    # create animated text effect using time.sleep() define as helper function
    print("Welcome to the puzzle Game!")

    # Instantiate puzzle and display to user
    game = Puzzle("https://i.pinimg.com/originals/4f/e7/06/4fe7066d4f3aa7201e38484230fc32b3.jpg")
    game.render_puzzle()
    player_won = False

    while not player_won:
        # Ask user which tile they would like to move and to what destination
        user_tile = input("What tile would you like to move?\t")
        user_destination = input("Where would you like to move it to")

        # move tile and update empty slot and movable tiles
        moved = game.move(int(user_tile), int(user_destination))
        if not moved:
            print("Choose a valid tile\n")
        else:
            game.render_puzzle()

        # check if player won
        player_won = game.check_if_player_won()

    game.start_win_sequence()
