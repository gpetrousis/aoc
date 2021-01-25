""" Day 15 Unit test """

from aoc2020 import day_15


seed = [0, 3, 6]


def test_parse_input():
    """ Test parse_input function """
    assert day_15.parse_input("./data/day15/test_input.txt") == seed


def test_find_number():
    """ Test find_number function """
    assert day_15.find_number.__wrapped__(seed, 4) == 0
    assert day_15.find_number.__wrapped__(seed, 5) == 3
    assert day_15.find_number.__wrapped__(seed, 6) == 3
    assert day_15.find_number.__wrapped__(seed, 7) == 1
    assert day_15.find_number.__wrapped__(seed, 8) == 0
    assert day_15.find_number.__wrapped__(seed, 9) == 4
    assert day_15.find_number.__wrapped__(seed, 10) == 0
    assert day_15.find_number.__wrapped__(seed, 2020) == 436

    # Commented out so the tests won't take forever to run
    # assert day_15.find_number([0,3,6], 30000000) == 175594
    # assert day_15.find_number([1,3,2], 30000000) == 2578
    # assert day_15.find_number([2,1,3], 30000000) == 3544142
    # assert day_15.find_number([1,2,3], 30000000) == 261214
    # assert day_15.find_number([2,3,1], 30000000) == 6895259
    # assert day_15.find_number([3,2,1], 30000000) == 18
    # assert day_15.find_number([3,1,2], 30000000) == 362
