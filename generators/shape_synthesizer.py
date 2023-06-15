def convert_shape_to_2d_array(shape):
    coord_shape = shape.split('\n')
    for i in range(len(coord_shape)):
        coord_shape[i] = list(coord_shape[i])
    return coord_shape

def get_border_points(shape_arr):
    # get all exterior points around shape
    border_points = []
    for i in range(len(shape_arr)):
        for j in range(len(shape_arr[i])):
            if shape_arr[i][j] != ' ':
                if i == 0 or i == len(shape_arr) - 1 or j == 0 or j == len(shape_arr[i]) - 1:
                    border_points.append((i, j))
                elif shape_arr[i-1][j] == ' ' or shape_arr[i+1][j] == ' ' or shape_arr[i][j-1] == ' ' or shape_arr[i][j+1] == ' ':
                    border_points.append((i, j))
    return border_points

def convert_points_to_shape(shape_arr):
    shape = ''
    for row in shape_arr:
        shape += ''.join(row) + '\n'
    shape = shape[:-1]
    return shape

def shift_coords(coords, x_shift, y_shift):
    shifted_coords = []
    for coord in coords:
        shifted_coords.append((coord[0] + y_shift, coord[1] + x_shift))
    return shifted_coords

def get_max_x_y(coords):
    max_x = 0
    max_y = 0
    for coord in coords:
        max_x = max(max_x, coord[1])
        max_y = max(max_y, coord[0])
    return (max_x, max_y)

def concat_shape_arrays(shape1, shape2):
    # find the max x and y of the first shape
    max_x, max_y = get_max_x_y(shape1)

    # find the max x and y of the second shape
    max_x2, max_y2 = get_max_x_y(shape2)

    # shift the second shape to be touching but not intersecting the first shape
    shape2 = shift_coords(shape2, max_x + 1, 0)

    # find the new max x and y of the second shape
    max_x2, max_y2 = get_max_x_y(shape2)

    # create new 2d array to hold both shapes
    final_shape = []
    for i in range(max(max_y, max_y2) + 1):
        final_shape.append([' '] * (max_x + max_x2 + 1))

    # fill in the first shape
    for coord in shape1:
        final_shape[coord[0]][coord[1]] = 'X'

    # fill in the second shape
    for coord in shape2:
        final_shape[coord[0]][coord[1]] = 'X'

    return final_shape

def generate_shape_combinations(shape1, shape2):
    # CONVERT shape1 into 2d array
    coord_shape = convert_shape_to_2d_array(shape1)
    coord_shape2 = convert_shape_to_2d_array(shape2)

    border1 = get_border_points(coord_shape)
    border2 = get_border_points(coord_shape2)

    return convert_points_to_shape(concat_shape_arrays(border1, border2))
