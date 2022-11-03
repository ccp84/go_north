import random

def build_story():
    storyline = []
    with open("positive.txt") as positive:
        for line in positive:
            new_line = line.strip('\n')
            storyline.append(new_line)
    random.shuffle(storyline)
    print(storyline)



build_story()