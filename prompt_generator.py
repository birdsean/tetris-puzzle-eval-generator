def print_shapes(shapes: list[str]):
    for shape in shapes:
        print(shape+'\n')

def gen_prompt(shapes: list[str], goal: str, answer: str):
    return f'''It's time to play a shape game! Your goal is to use arrange shapes you'll be given into a predefined form. If you can arrange them into the final form, you win! Here's an example:

Given shapes:

AAAA

BBB
  B

Please create:

XXXX
 XXX
   X

Answer:
AAAA
 BBB
   B


Now it's your turn.

Given shapes:

{print_shapes(shapes)}

Please create:

{goal}

Replacing the 'X's with the corresponding letter of the shape that should occupy each position. Only respond with the final shape, no commentary.

Answer:
{answer}'''

prompt = gen_prompt([
'AAA\n  A',
'BBB\nB',
'  C\nCCC',
'D\nDDD'
], 'XXXXXX\n  XX \n  XX\nXXXXXX', 'AAABBB\n  AB\n  CD\nCCCDDD')

print(prompt)