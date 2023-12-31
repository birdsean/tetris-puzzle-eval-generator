import random


def print_shapes(shapes: list[str]):
    # randomize order of shapes
    random.shuffle(shapes)
    shapes_str = ''
    for shape in shapes:
        shapes_str += shape + '\n\n'
    return shapes_str

def gen_prompt(shapes: list[str], goal: str):
    return f'''It's time to play a shape game! Your goal is to use arrange shapes you'll be given into a predefined form. If you can arrange them into the final form, you win! You may not rotate the shapes. Here's an example:

Given shapes:

 A
AA
A

B
BB
 B

Please create:

 XX
XXXX
X  X

Answer:

 AB
AABB
A  B

Now it's your turn.

Given shapes:

{print_shapes(shapes)}
Please create:

{goal}

Replacing the 'X's with the corresponding letter of the shape that should occupy each position. Please reason step by step before answering, and provide your final answer at the end, prefixed with 'Answer:' and a new line. For example: 

Answer:
 AB
AABB
A  B'''
