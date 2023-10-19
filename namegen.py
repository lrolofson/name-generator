import random

def listify(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

namesFirst = listify("first-names.txt")
namesLast = listify("last-names.txt")
namesSuffix = listify("last-name-suffixes.txt")

permuationCount = (len(namesFirst) * len(namesLast) * len(namesSuffix))

print("Currently there are " + str(len(namesFirst)) + " * " + str(len(namesLast)) + " * " + str(len(namesSuffix)) + " = " + str(permuationCount) + " possible combinations.")

for i in range(10):
    print(random.choice(namesFirst) + " " + random.choice(namesLast) + random.choice(namesSuffix))