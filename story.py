import random

def build_story():
    with open("positive.txt") as positive:
        for line in positive:
            new_line = line.strip('\n')
            print(new_line.split("*"))


build_story()