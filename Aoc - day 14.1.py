from collections import defaultdict

from matplotlib.pyplot import step


def read_file(file):
    pair = defaultdict()
    polymer_template = ""
    with open(file, "r") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) == 20:
                polymer_template = line
            elif line != "":
                pair[line[0:2]] = line[-1]
    return polymer_template, pair


def pair_insertion(polymer, pair_insertion, steps):
    new_polimer = ""
    for nro_of_step in range(steps + 1):
        for position in range(len(polymer)):
            if position == 1:
                new_polimer = (
                    polymer[0] + pair_insertion[polymer[0] + polymer[1]] + polymer[1]
                )
            else:
                new_polimer = (
                    new_polimer
                    + pair_insertion[polymer[position - 1] + polymer[position]]
                    + polymer[position]
                )
        polymer = new_polimer
    return new_polimer


def result(polymer):
    letters = list(set(polymer))
    letter_count = []
    for letter in letters:
        letter_count.append(polymer.count(letter))
    result = max(letter_count) - min(letter_count)
    return result


polymer, pairs = read_file(
    "/Users/bzabert/Documents/Python/Adevent of code/Day 14/AoC - day 14 - input.txt"
)
# print(polymer, pairs)
# print(pair_insertion(polymer, pairs, 9))
new_polymer = pair_insertion(polymer, pairs, 39)
print(result(new_polymer))
