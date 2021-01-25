""" Day 3: Toboggan Trajectory """
import os
from functools import reduce
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """ Parse the input into a 2D array """
    area = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            area.append(list(line.strip("\n")))

    return area


def traverse_area(area, step_x, step_y):
    """
    Traverse the area and count the
    number of tree that are encountered
    """
    # Assume that all the lines have the same length
    max_x = len(area[0])

    pos_x = step_x
    pos_y = step_y

    tree_count = 0
    while pos_y < len(area):
        if area[pos_y][pos_x] == "#":
            tree_count += 1

        pos_x = (pos_x + step_x) % max_x
        pos_y += step_y

    return tree_count


@timer
def part_1(area):
    """ Solve part 1 """
    return traverse_area(area, 3, 1)


@timer
def part_2(area):
    """ Solve part 2 """
    results = [
        traverse_area(area, 1, 1),
        traverse_area(area, 3, 1),
        traverse_area(area, 5, 1),
        traverse_area(area, 7, 1),
        traverse_area(area, 1, 2),
    ]

    return reduce((lambda x, y: x * y), results)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ Main function """
    area = parse_input(input_path)

    click.echo("Day 3: Toboggan Trajectory")
    click.echo(f"Part 1: {part_1(area)}")
    click.echo(f"Part 2: {part_2(area)}")
