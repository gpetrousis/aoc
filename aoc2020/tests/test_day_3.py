""" Day 3 Unit test """

# import click.testing
from aoc2020 import day_3

data = [
    [".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", "#", ".", ".", ".", "#", ".", "."],
    [".", "#", ".", ".", ".", ".", "#", ".", ".", "#", "."],
    [".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#"],
    [".", "#", ".", ".", ".", "#", "#", ".", ".", "#", "."],
    [".", ".", "#", ".", "#", "#", ".", ".", ".", ".", "."],
    [".", "#", ".", "#", ".", "#", ".", ".", ".", ".", "#"],
    [".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
    ["#", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#"],
    [".", "#", ".", ".", "#", ".", ".", ".", "#", ".", "#"],
]


def test_parse_input():
    """ Test parse_input function """
    assert day_3.parse_input("./data/day3/test_input.txt") == data


def test_traverse_area():
    """ Test traverse_area function """
    assert day_3.traverse_area(data, 1, 1) == 2
    assert day_3.traverse_area(data, 3, 1) == 7
    assert day_3.traverse_area(data, 5, 1) == 3
    assert day_3.traverse_area(data, 7, 1) == 4
    assert day_3.traverse_area(data, 1, 2) == 2
