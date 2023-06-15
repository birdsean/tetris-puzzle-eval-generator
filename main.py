import random
import generators.prompt_generator
import generators.shape_generator
import generators.shape_synthesizer

def pick_label_letters():
    # pick 2 different, random capital letters
    possible_letters = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    letter1 = random.choice(possible_letters)
    letter2 = random.choice(possible_letters)
    while letter1 == letter2:
        letter2 = random.choice(possible_letters)
    return letter1, letter2


shapes = generators.shape_generator.generate_shapes()

# get all unique pairs of shapes possible, no duplicates
shape_pairs = set()
for i in range(len(shapes)):
    for j in range(i+1, len(shapes)):
        # sort shapes alphabetically so that the order of the pair doesn't matter
        shape_pairs.add(tuple(sorted((shapes[i], shapes[j]))))

shape_pairs = random.sample(sorted(shape_pairs), 50)

# generate a prompt for each pair
prompts = []
for pair in shape_pairs:
    should_shift_x = random.choice([True, False])
    prompt_shape = generators.shape_synthesizer.generate_shape_combinations(pair[0], pair[1], should_shift_x)

    label1, label2 = pick_label_letters()
    lettered_shape_1 = pair[0].replace('X', label1)
    lettered_shape_2 = pair[1].replace('X', label2)

    answer_shape = generators.shape_synthesizer.generate_shape_combinations(lettered_shape_1, lettered_shape_2, should_shift_x)
    prompt = generators.prompt_generator.gen_prompt([lettered_shape_1, lettered_shape_2], prompt_shape, answer_shape)
    prompts.append(prompt)

# write prompts to txt file
with open('prompts.txt', 'w') as f:
    for prompt in prompts:
        f.write(prompt + '\n\n')
