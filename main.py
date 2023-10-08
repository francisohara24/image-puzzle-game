from PIL import Image
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
    slots  = {}
    empty_slot = 9
    movable_tiles = []

    def __init__(self, puzzle_image_path: str):
        # Read puzzle image
        self.image = Image.open(puzzle_image_path)

        # Divide image into list of 9 images
        tile_images = divide_image(self.image, 3,3)

        # construct 8 tiles from images
        for i in range(tile_images)[:-1]:
            random_positions = random_list_generator(8)
            right_position = i + 1
            random_position = random_positions[i]
            tile_id = random_position
            tile_image = tile_images[i]

            tile = Tile(tile_id, random_position, right_position, tile_image)
            self.slots[tile.position] = tile

        # set initial empty slot
        self.empty_slot = 9

        # set which tiles are movable based on initial empty slot
        self.update_movable_tiles()


    def update_movable_tiles(self):
        """update which tiles are movable and which are not based on the current empty slot."""

        # make all tiles immovable
        self.movable_tiles = []

        # update movable tiles based on empty slot
        match self.empty_slot:
            case 1:
                self.movable_tiles.extend([2, 4])
            case 2:
                self.movable_tiles.extend([1, 3, 5])
            case 3:
                self.movable_tiles.extend([2, 6])
            case 4:
                self.movable_tiles.extend([1, 5, 7])
            case 5:
                self.movable_tiles.extend([2, 4, 6, 8])
            case 6:
                self.movable_tiles.extend([3, 5, 9])
            case 7:
                self.movable_tiles.extend([4, 8])
            case 8:
                self.movable_tiles.extend([7, 5, 9])
            case 9:
                self.movable_tiles.extend([8, 6])

    def move(self, tile: Tile, position: int) -> None:
        """Move specified tile to specified position and update the current empty slot."""


    def check_winning_state(self):
        """Check if the current state of all tiles is the winning state."""


    def render_puzzle(self):
        pass




def play():
    """"""
    pass