import random

def listify(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

namesFirst = listify("first-names.txt")
namesLast = listify("last-names.txt")
namesSuffix = listify("last-name-suffixes.txt")

print(random.choice(namesFirst) + " " + random.choice(namesLast) + random.choice(namesSuffix))