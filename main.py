import random
import generators.prompt_generator
import generators.shape_generator
import generators.shape_synthesizer

shapes = generators.shape_generator.generate_shapes()

# get all unique pairs of shapes possible, no duplicates
shape_pairs = set()
for i in range(len(shapes)):
    for j in range(i+1, len(shapes)):
        # sort shapes alphabetically so that the order of the pair doesn't matter
        shape_pairs.add(tuple(sorted((shapes[i], shapes[j]))))

# pick 100 random pairs of shapes
shape_pairs = random.sample(sorted(shape_pairs), 100)

# generate a prompt for each pair
prompts = []
for pair in shape_pairs:
    prompt_shape = generators.shape_synthesizer.generate_shape_combinations(pair[0], pair[1])
    lettered_shape_1 = pair[0].replace('X', 'A')
    lettered_shape_2 = pair[1].replace('X', 'B')
    answer_shape = generators.shape_synthesizer.generate_shape_combinations(lettered_shape_1, lettered_shape_2)
    prompt = generators.prompt_generator.gen_prompt([lettered_shape_1, lettered_shape_2], prompt_shape, answer_shape)
    prompts.append(prompt)

# write prompts to txt file
with open('prompts.txt', 'w') as f:
    for prompt in prompts:
        f.write(prompt + '\n\n')
