""" Day 17: Conway Cubes """

import os
from itertools import product
from collections import defaultdict
import click
from aoc2020.timer import timer


def parse_input(input_path, dimentions):
    """Parse the input"""
    active_cubes = set()
    with open(os.path.abspath(input_path)) as input_file:
        for (index_y, line) in enumerate(input_file):
            for (index_x, value) in enumerate(line.rstrip("\n")):
                if value == "#":
                    coordinate = (index_x, index_y) + (0,) * (dimentions - 2)
                    active_cubes.add(coordinate)

    return active_cubes


def sum_coordinate(coordinate, diff):
    """ Sum diff to a coordinate """
    return tuple(sum(x) for x in zip(coordinate, diff))


def get_neighbour_indexes(coordinate, dimentions):
    """ Get the neighbours from a given index """
    diffs = list(product((-1, 0, 1), repeat=dimentions))
    return [sum_coordinate(coordinate, diff) for diff in diffs]


def cycle(active_cubes, dimentions):
    """ Play a cycle of the game """
    inactive_cubes = defaultdict(int)
    next_active = set()

    for coordinate in active_cubes:
        neighbour_indexes = get_neighbour_indexes(coordinate, dimentions)
        active_neighbours = [
            x for x in neighbour_indexes if x in active_cubes and x != coordinate
        ]
        inactive_neighbours = [x for x in neighbour_indexes if x not in active_cubes]

        if len(active_neighbours) in [2, 3]:
            next_active.add(coordinate)

        for inactive in inactive_neighbours:
            inactive_cubes[inactive] += 1

    for (coordinate, count) in inactive_cubes.items():
        if count == 3:
            next_active.add(coordinate)

    return next_active


@timer
def solve(grid, dimentions):
    """ Play 6 rounds of the game """
    next_cycle = grid
    for _ in range(6):
        next_cycle = cycle(next_cycle, dimentions)

    return len(next_cycle)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 17 Main """
    grid_3 = parse_input(input_path, 3)
    grid_4 = parse_input(input_path, 4)

    click.echo("Day 17: Conway Cubes")
    click.echo(f"Part 1: {solve(grid_3, 3)}")
    click.echo(f"Part 2: {solve(grid_4, 4)}")
