def build_story():
    with open("positive.csv") as positive:
        positive_file = csv.DictReader(positive)
        for row in positive_file:
            print(row)


build_story()