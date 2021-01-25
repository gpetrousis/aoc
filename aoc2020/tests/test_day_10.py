""" Day 10 Unit test """

from aoc2020 import day_10

parsed_input = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

small_input = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]


def test_parse_input():
    """ Test parse_input function """
    assert day_10.parse_input("./data/day10/test_input.txt") == parsed_input


def test_get_joltage_difference():
    """ Test get_joltage_difference function """
    assert day_10.get_joltage_difference.__wrapped__(small_input) == 35
    assert day_10.get_joltage_difference.__wrapped__(parsed_input) == 220


def test_get_joltage_arrangements():
    """ Test get_joltage_arrangements function """
    assert day_10.get_joltage_arrangements.__wrapped__(small_input) == 8
    assert day_10.get_joltage_arrangements.__wrapped__(parsed_input) == 19208
