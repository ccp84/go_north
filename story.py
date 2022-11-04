import random
import json
import ast


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
        """
        ast.literal_eval code used from stack overflow
        to solve issue of apostrophes being added when
        importing list into dictionary turning it into
        a string object. See readme credits for link.
        """
        storyline[current_level] = {
            "a": ast.literal_eval(level_options[0]),
            "b": ast.literal_eval(level_options[1]),
            "c": ast.literal_eval(level_options[2]),
            "d": ast.literal_eval(level_options[3])
        }
        current_level += 1
    winning = []
    ending = []
    with open("winners.txt") as winners:
        for line in winners:
            new_line = line.strip('\n')
            winning.append(new_line)
    random.shuffle(winning)
    ending.extend([winning[0],
                   winning[1],
                   negatives[current_level],
                   negatives[current_level + 1]])
    storyline[current_level] = {
        "a": ast.literal_eval(ending[0]), 
        "b": ast.literal_eval(ending[1]), 
        "c": ast.literal_eval(ending[2]),
        "d": ast.literal_eval(ending[3])
    }
    return storyline


build_story()
