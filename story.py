import random


def build_story():
    positives = []
    negatives = []
    with open("positive.txt") as positive:
        for line in positive:
            new_line = line.strip('\n')
            positives.append(new_line)
    with open("negative.txt") as negative:
        for line in negative:
            new_line = line.strip('\n')
            negatives.append(new_line)
    random.shuffle(positives)
    random.shuffle(negatives)
    current_level = 1
    storyline = {}
    while current_level < 4:
        level_options = []
        i = 1
        while i <= 3:
            level_options.append(positives[i + (i * current_level)])
            i += 1
        level_options.append(negatives[current_level])
        random.shuffle(level_options)
        storyline[current_level] = {
            "a": level_options[0], "b": level_options[1], "c": level_options[2], "d": level_options[3]
            }
        current_level += 1
    #ending = []
    # with open("winners.txt") as winners:
    #     for line in winners:
    #         new_line = line.strip('\n')
    #         ending.append(new_line)
    # random.shuffle(ending)
    # storyline[current_level] = {

    # }
    print(storyline)


build_story()
