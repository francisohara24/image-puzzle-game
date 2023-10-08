"""Helper functions for manipulating images."""
from PIL import Image
from random import randint

def divide_image( input_image: Image, rows: int, columns: int) -> list[Image]:
    """Divide `input_image` into `rows` x `columns` pieces and return a list of the pieces."""
    pieces = []  # list of resulting image pieces
    total_width, total_height = input_image.size # input image dimensions
    piece_width = total_width // columns  # width of each piece
    piece_height = total_height // rows  # height of each piece

    # define initial cropping coordinates
    left = 0
    upper = 0
    right = piece_width
    lower = piece_height

    # crop image into pieces
    for row in range(rows):
        for column in range(columns):
            # crop image piece and append to list of pieces
            piece = input_image.crop((left, upper, right, lower))
            pieces.append(piece)

            # update cropping coordinates for next column
            left += piece_width
            right += piece_width

    # update cropping coordinates for next row
    left = 0
    right = 0
    upper += piece_height
    lower += piece_height

    return pieces


def random_list_generator(b: int) -> list[int]:
    """Return a list of `b` random integers within the range of 1 to `b` inclusive.
    The randomness is in the position of each number in the list."""
    numbers = []
    while len(numbers) < b:
        number = randint(1, b)
        if number not in numbers:
            numbers.append(number)

    return numbers

# test each helper function
if __name__ == "__main__":
    print(random_list_generator(10))