""" Day 8 Unit test """

from aoc2020 import day_8

parsed_input = [
    ("nop", 0),
    ("acc", 1),
    ("jmp", 4),
    ("acc", 3),
    ("jmp", -3),
    ("acc", -99),
    ("acc", 1),
    ("jmp", -4),
    ("acc", 6),
]


def test_parse_input():
    """ Test parse_input function """
    assert day_8.parse_input("./data/day8/test_input.txt") == parsed_input


def test_run_commands():
    """ Test parse_input function """
    assert day_8.run_commands(parsed_input) == (False, 5)


def test_fix_commands():
    """ Test parse_input function """
    assert day_8.fix_commands(parsed_input) == 8
