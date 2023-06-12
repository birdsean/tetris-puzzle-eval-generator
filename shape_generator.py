# This script generates rectangular shapes composed of tetris-like shapes
# Each shape is distinguished by a unique capital letter, starting with 'A'
# The script outputs the shapes in a text file, with the following format:
# "AAAA"""B\nBBB"+"CCC\nC"="AAAA\nBCCC\nBBBC"
# It takes parameters "length" and "width" of the rectangle and tries to minimize the number of 4 pieced shapes that compose that rectangle

import random
MAX_SHAPE_SIZE = 4

seed_shapes = [
    'AAAA',
    'A\nAAA',
    'AAA\n  A',
    'AA\nAA',
    'A\nAA\nA',
    ' AA\nAA',
    'AA\n AA',
]

# pick a random seed shape
def pick_seed_shape():
    return seed_shapes[random.randint(0, len(seed_shapes) - 1)]

def rotate_shape(shape: str):
    shape = shape.split('\n')

    # init 2d array that is max_length x max_length
    rotated_shape = []
    for i in range(MAX_SHAPE_SIZE):
        rotated_shape.append([' '] * MAX_SHAPE_SIZE)

    # fill in rotated shape
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            rotated_shape[j][len(shape) - i - 1] = shape[i][j]

    # convert rotated shape to string
    rotated_shape_str = ''
    for row in rotated_shape:
        rotated_shape_str += ''.join(row) + '\n'
    rotated_shape_str = rotated_shape_str[:-1]

    return rotated_shape_str

def spin_shape(shape, rotations):
    for i in range(rotations):
        shape = rotate_shape(shape)

    # trim down string to bounding box
    shape = shape.split('\n')
    min_x = MAX_SHAPE_SIZE
    min_y = MAX_SHAPE_SIZE
    max_x = 0
    max_y = 0
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] != ' ':
                min_x = min(min_x, j)
                min_y = min(min_y, i)
                max_x = max(max_x, j)
                max_y = max(max_y, i)
    
    shape = shape[min_y:max_y+1]
    for i in range(len(shape)):
        shape[i] = shape[i][min_x:max_x+1]
    shape = '\n'.join(shape)
    return shape

possible_shapes = set()

for shape in seed_shapes:
    possible_shapes.add(shape)
    for i in range(4):
        possible_shapes.add(spin_shape(shape, i))

for shape in sorted(possible_shapes):
    print(shape)
    print()
