import random
import json
import ast


def build_story():
    positives = []
    negatives = []
    """
    Read in positive/negative text file,
    Create a new list of each line
    Shuffle
    """
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
    """
    Initialise level and blank storyline dictionary
    Loop creates each level as a list of 3 positive, 1 negative
    Shuffle, then add level to storyline
    Increment level indicator until full story - 1 has been built
    """
    current_level = 1
    storyline = {}
    while current_level < 5:
        level_options = []
        level_options.extend([positives.pop(),
                              positives.pop(),
                              positives.pop(),
                              negatives.pop()])
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
    """
    Open and read in winning options text file, shuffle.
    Create a container for final level.
    Build final level containing 2 winning, 2 negative options.
    Shuffle ending level and add to storyline dictionary
    """
    winning = []
    ending = []
    with open("winners.txt") as winners:
        for line in winners:
            new_line = line.strip('\n')
            winning.append(new_line)
    random.shuffle(winning)
    ending.extend([winning.pop(),
                   winning.pop(),
                   negatives.pop(),
                   negatives.pop()])
    random.shuffle(ending)
    storyline[current_level] = {
        "a": ast.literal_eval(ending[0]),
        "b": ast.literal_eval(ending[1]),
        "c": ast.literal_eval(ending[2]),
        "d": ast.literal_eval(ending[3])
    }
    return storyline


build_story()
