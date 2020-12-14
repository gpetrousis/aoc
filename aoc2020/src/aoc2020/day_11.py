""" AOC Day 11 """
import os
from copy import deepcopy
import click


OFFSETS = [
    (-1, -1),  # Top-Left
    (-1, 0),  # Top
    (-1, 1),  # Top-Right
    (0, 1),  # Right
    (1, 1),  # Right-Bottom
    (1, 0),  # Bottom
    (1, -1),  # Left-Bottom
    (0, -1),  # Left
]


def parse_input(input_path):
    """Read the input file and parse it into a 2d array"""
    area = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            area.append(list(line.rstrip("\n")))

    return area


def count_seats(area, x, y, deep = False):
    """Count the taken seats around the current seat"""
    rows = len(area)
    columns = len(area[0])

    acc = 0
    for (step_y, step_x) in OFFSETS:
        current_x = x + step_x
        current_y = y + step_y
        while 0 <= current_y < rows and 0 <= current_x < columns:
            if area[current_y][current_x] == "L":
                break

            if area[current_y][current_x] == "#":
                acc += 1
                break

            current_x += step_x
            current_y += step_y

            if not deep:
                break

    return acc


def step(area, limit, deep = False):
    """Play a round of seat taking"""
    new_area = deepcopy(area)

    for (y, row) in enumerate(area):
        for (x, value) in enumerate(row):
            if value == "L" and count_seats(area, x, y, deep) == 0:
                new_area[y][x] = "#"

            elif value == "#" and count_seats(area, x, y, deep) >= limit:
                new_area[y][x] = "L"

    return new_area


def play(area, limit, deep = False):
    """Play the seats game and return the number of occupied seats"""
    current_area = area
    while True:
        next_area = step(current_area, limit, deep)
        if current_area == next_area:
            return sum(map(lambda x: x.count("#"), current_area))

        current_area = next_area

    return None


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 11 Main """
    area = parse_input(input_path)

    click.echo(play(area, 4, False))
    click.echo(play(area, 5, True))

