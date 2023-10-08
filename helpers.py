"""Helper functions for manipulating images."""
from PIL import Image


def divide_image(self, input_image: Image, rows, columns):
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

