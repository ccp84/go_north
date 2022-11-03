import random

def build_story():
    storyline = []
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
    print(positives[0])
    print(negatives)



build_story()