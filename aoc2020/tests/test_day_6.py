""" Day 6 Unit test """

from aoc2020 import day_6

data = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]


group = [
    "abcx",
    "abcy",
    "abcz",
]


def test_parse_input():
    """ Test parse_input function """
    assert day_6.parse_input("./data/day6/test_input.txt") == data


def test_get_group_answers():
    """ Test get_group_answers function """
    assert day_6.get_group_answers(group) == set(["a", "b", "c", "x", "y", "z"])
    assert day_6.get_group_answers(data[0]) == set(["a", "b", "c"])
    assert day_6.get_group_answers(data[1]) == set(["a", "b", "c"])
    assert day_6.get_group_answers(data[2]) == set(["a", "b", "c"])
    assert day_6.get_group_answers(data[3]) == set(["a"])
    assert day_6.get_group_answers(data[4]) == set(["b"])


def test_get_common_group_answers():
    """ Test get_group_answers function """
    assert day_6.get_common_group_answers(group) == set(["a", "b", "c"])
    assert day_6.get_common_group_answers(data[0]) == set(["a", "b", "c"])
    assert day_6.get_common_group_answers(data[1]) == set()
    assert day_6.get_common_group_answers(data[2]) == set(["a"])
    assert day_6.get_common_group_answers(data[3]) == set(["a"])
    assert day_6.get_common_group_answers(data[4]) == set(["b"])


def test_count_answers():
    """ Test count_all_answers function """
    assert day_6.count_answers.__wrapped__(data, day_6.get_group_answers) == 11
    assert day_6.count_answers.__wrapped__(data, day_6.get_common_group_answers) == 6
