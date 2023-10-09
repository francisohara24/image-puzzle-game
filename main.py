from PIL import Image
from IPython.display import display
from helpers import divide_image, random_list_generator

class Tile:
    tile_id = None
    position = None
    right_position = None
    image = None

    def __init__(self, tile_id: int, position: int, right_position: int, image: Image):
        self.tile_id = tile_id
        self.position = position
        self.right_position = right_position # the correct position of the tile in the puzzle
        self.image = image


    def render(self):
        pass

class Puzzle:
    image = None
    tiles  = {}
    empty_position = None
    movable_positions = []

    def __init__(self, puzzle_image_path: str):
        # Read puzzle image
        self.image = Image.open(puzzle_image_path)

        # Divide image into list of 9 images
        tile_images = divide_image(self.image, 3,3)

        # construct 8 tiles from images
        for i in range(len(tile_images) - 1):
            random_positions = random_list_generator(8)
            right_position = i + 1
            random_position = random_positions[i]
            tile_id = random_position
            tile_image = tile_images[i]

            tile = Tile(tile_id, random_position, right_position, tile_image)
            self.tiles[tile.tile_id] = tile

        # set initial empty position
        self.empty_position = 9

        # set which tiles are movable based on initial empty position
        self.update_movable_tiles()


    def update_movable_tiles(self):
        """update which tiles are movable and which are not based on the current empty slot."""

        # make all tiles immovable
        self.movable_positions = []

        # update movable tiles based on empty position
        match self.empty_position:
            case 1:
                self.movable_positions.extend([2, 4])
            case 2:
                self.movable_positions.extend([1, 3, 5])
            case 3:
                self.movable_positions.extend([2, 6])
            case 4:
                self.movable_positions.extend([1, 5, 7])
            case 5:
                self.movable_positions.extend([2, 4, 6, 8])
            case 6:
                self.movable_positions.extend([3, 5, 9])
            case 7:
                self.movable_positions.extend([4, 8])
            case 8:
                self.movable_positions.extend([7, 5, 9])
            case 9:
                self.movable_positions.extend([8, 6])

    def move(self, tile_id: int, new_position: int) -> bool:
        """Move specified tile to specified position and update the current empty slot."""
        # check if tile_id and new_position are valid values
        # if ....
        # else: return False

        tile_position = self.tiles[tile_id].position # position of tile to be moved

        # check if new position is empty and tile is movable
        if new_position == self.empty_position and tile_position in self.movable_positions:
            self.tiles[tile_id].position = new_position   # set tile position to new_position
            self.empty_position = tile_position   # set new empty position for the puzzle

        else:
            return False

        # update list of movable tiles
        self.update_movable_tiles()

        return True

    def check_if_player_won(self):
        """Check if player won (i.e. if all tiles are in the right position)"""
        player_won = True
        for tile in self.tiles.values():
            if tile.position != tile.right_position:
                player_won = False
                break
        return player_won


    def render_puzzle(self):
        print("puzzle rendered.")

    def start_win_sequence(self):
        """Write images and text to congratulate the player"""
        win_message = """
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                                                                                                                             
"""
        print(win_message)
        # render winning image
        # display time taken to solve puzzle in winning image


def play():
    """Start the main game sequence"""

    # Welcome the user to the game
    # create animated text effect using time.sleep() define as helper function
    print("Welcome to the puzzle Game!")

    # Instantiate puzzle and display to user
    game = Puzzle("data/puzzle_img_1.jpg")
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



