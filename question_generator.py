import random
import shape_generator

shapes = shape_generator.generate_shapes()
COUNT_QUESTIONS = 2
for i in range(COUNT_QUESTIONS):
    # pick a random shape
    shape = shapes[random.randint(0, len(shapes) - 1)]

    # pick a second shape that is not the same as the first
    shape2 = shape
    while shape2 == shape:
        shape2 = shapes[random.randint(0, len(shapes) - 1)]

    # cover shape1 into 2d array
    coord_shape = shape.split('\n')
    for i in range(len(coord_shape)):
        coord_shape[i] = list(coord_shape[i])

    # find all coords where shape1 is not empty
    coords = []
    for i in range(len(coord_shape)):
        for j in range(len(coord_shape[i])):
            if coord_shape[i][j] != ' ':
                coords.append((i, j))

    # pick a random coord
    rand_coord = coords[random.randint(0, len(coords) - 1)]

    # append shape2 to shape1 at that coord
    final_shape = coord_shape

    # add 3 to len and height of final_shape
    for i in range(len(final_shape)):
        final_shape[i] += [' '] * 3
    final_shape += [[' '] * len(final_shape[0])] * 3

    coord_shape2 = shape2.split('\n')
    for i in range(len(coord_shape2)):
        for j in range(len(coord_shape2[i])):
            if coord_shape2[i][j] != ' ':
                final_shape[rand_coord[0] + i][rand_coord[1] + j] = coord_shape2[i][j]
    
    # convert final shape to string
    final_shape_str = ''
    for row in final_shape:
        final_shape_str += ''.join(row) + '\n'

    print(shape)
    print('+')
    print(shape2)
    print('=')
    print(final_shape_str)
    print('\n\n')
    print("***********************")

    