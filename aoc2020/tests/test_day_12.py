""" Day 12 Unit test """

from aoc2020 import day_12

instructions = [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]


def test_parse_input():
    """ Test parse_input function """
    assert day_12.parse_input("./data/day12/test_input.txt") == instructions


def test_turn_ship():
    """ Test turn_ship function """
    assert day_12.turn(0, "R", 90) == 1
    assert day_12.turn(0, "R", 180) == 2
    assert day_12.turn(0, "R", 270) == 3
    assert day_12.turn(0, "R", 360) == 0
    assert day_12.turn(1, "L", 90) == 0
    assert day_12.turn(1, "L", 180) == 3
    assert day_12.turn(1, "L", 270) == 2
    assert day_12.turn(1, "L", 360) == 1


def test_step():
    """ Test step function """
    assert day_12.step("N", 3) == (0, 3)
    assert day_12.step("E", 5) == (5, 0)
    assert day_12.step("W", 10) == (-10, 0)
    assert day_12.step("S", 12) == (0, -12)


def test_move_ship():
    """ Test move_ship function """
    assert day_12.move_ship.__wrapped__(instructions) == 25


def test_move_waypoint():
    """ Test move_waypoint function """
    assert day_12.move_waypoint.__wrapped__(instructions) == 286
