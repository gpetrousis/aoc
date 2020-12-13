""" Day 9 Unit test """

from aoc2020 import day_9

parsed_input = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_parse_input():
    """ Test parse_input function """
    assert day_9.parse_input("./data/day9/test_input.txt") == parsed_input


def test_is_sum_of_data():
    """ Test is_sum_of_data_function function """
    data = [1721, 979, 366, 299, 675, 1456]
    assert day_9.is_sum_of_data(data, 2020)


def test_find_invalid_number():
    """ Test is_sum_of_data_function function """
    assert day_9.find_invalid_number(parsed_input, 5) == 127


def test_find_weekness():
    """ Test is_sum_of_data_function function """
    assert day_9.find_weekness(parsed_input, 127) == 62
