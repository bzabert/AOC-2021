from collections import defaultdict
from unittest import result
from matplotlib import axis
import numpy as np


def read_input(file):
    data = []
    dots = []
    orders = []
    with open(file) as file:
        for line in file.readlines():
            data.append(line.strip().split(","))
    for value in data:
        if len(value) == 2:
            dots.append(list(map(int, value)))
        elif value == [""]:
            pass
        else:
            value = value[0]
            value = value.strip("fold along ")
            value = value.split("=")
            orders.append([value[0], int(value[1])])

    return dots, orders


def create_map(list_dots):
    x = []
    y = []
    for dot in list_dots:
        x.append(dot[0])
        y.append(dot[1])
    array = [0] * (max(x) + 1)
    array = np.array([array] * (max(y) + 1))
    for dot in list_dots:
        array[dot[1]][dot[0]] = 1
    return array


def fold(map, folds):
    for fold in folds:
        if fold[0] == "y":
            half_1 = map[0 : (fold[1])]
            half_2 = map[(fold[1] + 1) :]
            half_2 = half_2[::-1]
            if len(half_1) > len(half_2):
                mat_zero = np.zeros(
                    [(len(half_1) - len(half_2)), len(half_1[0])], dtype=int
                )
                half_2 = np.append(mat_zero, half_2, axis=0)
            elif len(half_1) < len(half_2):
                mat_zero = np.zeros(
                    [(len(half_2) - len(half_1)), len(half_1[0])], dtype=int
                )
                half_1 = np.append(mat_zero, half_1, axis=0)
            map = np.add(half_1, half_2)
        if fold[0] == "x":
            half_1 = []
            half_2 = []
            for line in map:
                line_2 = line[(fold[1] + 1) :]
                line_1 = line[: (fold[1])]
                line_1 = line_1[::-1]
                if len(line_2) > len(line_1):
                    for i in range(len(line_2) - len(line_1)):
                        line_1 = np.append(line_1, 0)
                elif len(line_2) < len(line_1):
                    for i in range(len(line_1) - len(line_2)):
                        line_2 = np.append(line_2, 0)
                half_2.append(line_2)
                half_1.append(line_1)
            map = np.add(half_1, half_2)
    return map


def change_dots(map):
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] != 0:
                map[x][y] = 1

    return map


all_dots, folds = read_input(
    "/Users/bzabert/Documents/Python/Adevent of code/Day 13/AoC - day 13 - input.txt"
)
map = create_map(all_dots)
folds = fold(map, folds)
# print(map)
# print(folds)
result = change_dots(folds)
print(result)