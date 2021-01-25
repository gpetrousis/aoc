""" Day 13 Unit test """

from aoc2020 import day_13

ARRIVAL = 939
busses = [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]


def test_parse_input():
    """ Test parse_input function """
    assert day_13.parse_input("./data/day13/test_input.txt") == (ARRIVAL, busses)


def test_find_next_bus():
    """ Test parse_input function """
    assert day_13.find_next_bus.__wrapped__(ARRIVAL, busses) == 295


def test_chinese_remainder():
    """ Test chinese_remainder function """
    busses1 = [(17, 0), (13, 2), (19, 3)]
    busses2 = [(67, 0), (7, 1), (59, 2), (61, 3)]
    busses3 = [(67, 0), (7, 2), (59, 3), (61, 4)]
    busses4 = [(67, 0), (7, 1), (59, 3), (61, 4)]
    busses5 = [(1789, 0), (37, 1), (47, 2), (1889, 3)]

    assert day_13.chinese_remainder.__wrapped__(busses) == 1068781
    assert day_13.chinese_remainder.__wrapped__(busses1) == 3417
    assert day_13.chinese_remainder.__wrapped__(busses2) == 754018
    assert day_13.chinese_remainder.__wrapped__(busses3) == 779210
    assert day_13.chinese_remainder.__wrapped__(busses4) == 1261476
    assert day_13.chinese_remainder.__wrapped__(busses5) == 1202161486
