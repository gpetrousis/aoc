""" Day 1 Unit test """

from aoc2020 import day_1

data = [1721, 979, 366, 299, 675, 1456]
sorted_data = sorted(data)


def test_parse_input():
    """ Test parse_input function """
    assert day_1.parse_input("./data/day1/test_input.txt") == data


def test_get_sum_two():
    """ Test get_sum_two function """
    assert day_1.get_sum_two.__wrapped__(sorted_data, 2020) == 514579


def test_get_sum_three():
    """ Test get_sum_three function """
    assert day_1.get_sum_three.__wrapped__(sorted_data, 2020) == 241861950
