""" Day 24: Lobby Layout """
import os
from copy import copy
from collections import defaultdict
import click
from aoc2020.timer import timer


diffs = [
    (0, -1),  # nw
    (1, -1),  # ne
    (1, 0),  # e
    (0, 1),  # se
    (-1, 1),  # sw
    (-1, 0),  # w
]


def parse_input(input_path):
    """Parse the input"""
    tiles = []
    with open(os.path.abspath(input_path)) as input_file:
        tiles = [x.strip() for x in input_file]

    return tiles


def parse_tile(raw_tile):
    """ Parse a tile and return its position """
    tile = copy(raw_tile)
    pos_x = 0
    pos_y = 0
    while tile != "":
        if tile.startswith("e"):
            pos_x += 1
            tile = tile[1:]
        elif tile.startswith("se"):
            pos_y += 1
            tile = tile[2:]
        elif tile.startswith("sw"):
            pos_y += 1
            pos_x -= 1
            tile = tile[2:]
        elif tile.startswith("w"):
            pos_x -= 1
            tile = tile[1:]
        elif tile.startswith("nw"):
            pos_y -= 1
            tile = tile[2:]
        elif tile.startswith("ne"):
            pos_y -= 1
            pos_x += 1
            tile = tile[2:]

    return (pos_x, pos_y)


def flip_initial(tiles):
    """ Flip the initial tiles """
    black_tiles = set()

    for tile in tiles:
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return black_tiles


def sum_coordinate(coordinate, diff):
    """ Sum the diff to a coordinate """
    return tuple(sum(x) for x in zip(coordinate, diff))


def get_adjacent_tiles(tile):
    """ Get all the adjacent tiles """
    return [sum_coordinate(tile, diff) for diff in diffs]


def flip_tiles(black_tiles, days):
    """ Flip the tiles """
    _black_tiles = copy(black_tiles)

    for _ in range(days):
        next_black = set()
        white_tiles = defaultdict(int)

        for black_tile in _black_tiles:
            adjacent = get_adjacent_tiles(black_tile)
            black_adjacent = [x for x in adjacent if x in _black_tiles]
            white_adjacent = [x for x in adjacent if x not in _black_tiles]

            if len(black_adjacent) in [1, 2]:
                next_black.add(black_tile)

            for white_tile in white_adjacent:
                white_tiles[white_tile] += 1

        for (white_tile, count) in white_tiles.items():
            if count == 2:
                next_black.add(white_tile)

        _black_tiles = copy(next_black)

    return _black_tiles


@timer
def part_1(tiles):
    """ Solve part 1 """
    return len(flip_initial(tiles))


@timer
def part_2(tiles):
    """ Solve part 2 """
    black_tiles = flip_initial(tiles)
    return len(flip_tiles(black_tiles, 100))


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 24 Main """
    raw_tiles = parse_input(input_path)
    tiles = list(map(parse_tile, raw_tiles))

    click.echo("Day 24: Lobby Layout")
    click.echo(f"Part 1: {part_1(tiles)}")
    click.echo(f"Part 2: {part_2(tiles)}")
