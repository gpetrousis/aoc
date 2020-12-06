""" Day 5 Unit test """

from aoc2020 import day_5

data = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",
]


def test_parse_input():
    """ Test parse_input function """
    assert day_5.parse_input("./data/day5/test_input.txt") == data


def test_parse_code():
    """ Test parse_code function """
    assert day_5.parse_code("FBFBBFF", 0, 127) == 44
    assert day_5.parse_code("RLR", 0, 7) == 5


def test_parse_code_binary():
    """ Test parse_code function """
    assert day_5.parse_code_binary("FBFBBFF") == 44
    assert day_5.parse_code_binary("RLR") == 5


def test_parse_seat():
    """ Test parse_seat function """
    assert day_5.parse_seat(data[0]) == [70, 7]
    assert day_5.parse_seat(data[1]) == [14, 7]
    assert day_5.parse_seat(data[2]) == [102, 4]


def test_get_seat_id():
    """ Test get_seat_id function """
    assert day_5.get_seat_id(data[0]) == 567
    assert day_5.get_seat_id(data[1]) == 119
    assert day_5.get_seat_id(data[2]) == 820


def test_get_max_seat_id():
    """ Test get_max_seat_id function """
    assert day_5.get_max_seat_id(data) == 820
