""" Day 11 Unit test """

from aoc2020 import day_11

area = [
    ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
    ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
    ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
    ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
    ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
    [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
    ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
]


def test_parse_input():
    """ Test parse_input function """
    assert day_11.parse_input("./data/day11/test_input.txt") == area


def test_step():
    """ Test step with adjucent count function """
    step_0 = [
        ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", ".", "#", "#"],
        ["#", ".", "#", ".", "#", ".", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "#"],
        [".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "#"],
    ]

    step_1 = [
        ["#", ".", "L", "L", ".", "L", "#", ".", "#", "#"],
        ["#", "L", "L", "L", "L", "L", "L", ".", "L", "#"],
        ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
        ["#", "L", "L", "L", ".", "L", "L", ".", "L", "#"],
        ["#", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["#", ".", "L", "L", "L", "L", "#", ".", "#", "#"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["#", "L", "L", "L", "L", "L", "L", "L", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["#", ".", "#", "L", "L", "L", "L", ".", "#", "#"],
    ]

    step_2 = [
        ["#", ".", "#", "#", ".", "L", "#", ".", "#", "#"],
        ["#", "L", "#", "#", "#", "L", "L", ".", "L", "#"],
        ["L", ".", "#", ".", "#", ".", ".", "#", ".", "."],
        ["#", "L", "#", "#", ".", "#", "#", ".", "L", "#"],
        ["#", ".", "#", "#", ".", "L", "L", ".", "L", "L"],
        ["#", ".", "#", "#", "#", "L", "#", ".", "#", "#"],
        [".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
        ["#", "L", "#", "#", "#", "#", "#", "#", "L", "#"],
        ["#", ".", "L", "L", "#", "#", "#", "L", ".", "L"],
        ["#", ".", "#", "L", "#", "#", "#", ".", "#", "#"],
    ]

    step_3 = [
        ["#", ".", "#", "L", ".", "L", "#", ".", "#", "#"],
        ["#", "L", "L", "L", "#", "L", "L", ".", "L", "#"],
        ["L", ".", "L", ".", "L", ".", ".", "#", ".", "."],
        ["#", "L", "L", "L", ".", "#", "#", ".", "L", "#"],
        ["#", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["#", ".", "L", "L", "#", "L", "#", ".", "#", "#"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["#", "L", "#", "L", "L", "L", "L", "#", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["#", ".", "#", "L", "#", "L", "#", ".", "#", "#"],
    ]

    step_4 = [
        ["#", ".", "#", "L", ".", "L", "#", ".", "#", "#"],
        ["#", "L", "L", "L", "#", "L", "L", ".", "L", "#"],
        ["L", ".", "#", ".", "L", ".", ".", "#", ".", "."],
        ["#", "L", "#", "#", ".", "#", "#", ".", "L", "#"],
        ["#", ".", "#", "L", ".", "L", "L", ".", "L", "L"],
        ["#", ".", "#", "L", "#", "L", "#", ".", "#", "#"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["#", "L", "#", "L", "#", "#", "L", "#", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["#", ".", "#", "L", "#", "L", "#", ".", "#", "#"],
    ]
    assert day_11.step(area, 4) == step_0
    assert day_11.step(step_0, 4) == step_1
    assert day_11.step(step_1, 4) == step_2
    assert day_11.step(step_2, 4) == step_3
    assert day_11.step(step_3, 4) == step_4
    assert day_11.step(step_4, 4) == step_4


def test_step_deep():
    """ Test step with adjucent count function """
    step_0 = [
        ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", ".", "#", "#"],
        ["#", ".", "#", ".", "#", ".", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "#"],
        [".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "#"],
    ]

    step_1 = [
        ["#", ".", "L", "L", ".", "L", "L", ".", "L", "#"],
        ["#", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
        ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
        ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["L", "L", "L", "L", "L", "L", "L", "L", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
        ["#", ".", "L", "L", "L", "L", "L", ".", "L", "#"],
    ]

    step_2 = [
        ["#", ".", "L", "#", ".", "#", "#", ".", "L", "#"],
        ["#", "L", "#", "#", "#", "#", "#", ".", "L", "L"],
        ["L", ".", "#", ".", "#", ".", ".", "#", ".", "."],
        ["#", "#", "L", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", ".", "#", "L", ".", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "L"],
        [".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
        ["L", "L", "L", "#", "#", "#", "#", "L", "L", "#"],
        ["#", ".", "L", "#", "#", "#", "#", "#", ".", "L"],
        ["#", ".", "L", "#", "#", "#", "#", ".", "L", "#"],
    ]

    step_3 = [
        ["#", ".", "L", "#", ".", "L", "#", ".", "L", "#"],
        ["#", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "#", ".", "."],
        ["#", "#", "L", "L", ".", "L", "L", ".", "L", "#"],
        ["L", ".", "L", "L", ".", "L", "L", ".", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
        [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
        ["L", "L", "L", "L", "L", "L", "L", "L", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "#", ".", "L"],
        ["#", ".", "L", "#", "L", "L", "#", ".", "L", "#"],
    ]

    step_4 = [
        ["#", ".", "L", "#", ".", "L", "#", ".", "L", "#"],
        ["#", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "#", ".", "."],
        ["#", "#", "L", "#", ".", "#", "L", ".", "L", "#"],
        ["L", ".", "L", "#", ".", "#", "L", ".", "L", "#"],
        ["#", ".", "L", "#", "#", "#", "#", ".", "L", "L"],
        [".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
        ["L", "L", "L", "#", "#", "#", "L", "L", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "#", ".", "L"],
        ["#", ".", "L", "#", "L", "L", "#", ".", "L", "#"],
    ]
    step_5 = [
        ["#", ".", "L", "#", ".", "L", "#", ".", "L", "#"],
        ["#", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ["L", ".", "L", ".", "L", ".", ".", "#", ".", "."],
        ["#", "#", "L", "#", ".", "#", "L", ".", "L", "#"],
        ["L", ".", "L", "#", ".", "L", "L", ".", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "#", ".", "L", "L"],
        [".", ".", "#", ".", "L", ".", ".", ".", ".", "."],
        ["L", "L", "L", "#", "#", "#", "L", "L", "L", "#"],
        ["#", ".", "L", "L", "L", "L", "L", "#", ".", "L"],
        ["#", ".", "L", "#", "L", "L", "#", ".", "L", "#"],
    ]

    assert day_11.step(area, 5, True) == step_0
    assert day_11.step(step_0, 5, True) == step_1
    assert day_11.step(step_1, 5, True) == step_2
    assert day_11.step(step_2, 5, True) == step_3
    assert day_11.step(step_3, 5, True) == step_4
    assert day_11.step(step_4, 5, True) == step_5
    assert day_11.step(step_5, 5, True) == step_5


def test_count_seats():
    """ Test count_seats function"""
    case_0 = [
        [".", "#", "#", ".", "#", "#", "."],
        ["#", ".", "#", ".", "#", ".", "#"],
        ["#", "#", ".", ".", ".", "#", "#"],
        [".", ".", ".", "L", ".", ".", "."],
        ["#", "#", ".", ".", ".", "#", "#"],
        ["#", ".", "#", ".", "#", ".", "#"],
        [".", "#", "#", ".", "#", "#", "."],
    ]

    case_1 = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "L", ".", "L", ".", "#", ".", "#", ".", "#", ".", "#", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    case_2 = [
        [".", ".", ".", ".", ".", ".", ".", "#", "."],
        [".", ".", ".", "#", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "#", "L", ".", ".", ".", ".", "#"],
        [".", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "#", ".", ".", ".", ".", "."],
    ]

    assert day_11.count_seats(case_0, 3, 3, False) == 0
    assert day_11.count_seats(case_1, 1, 1, False) == 0
    assert day_11.count_seats(case_2, 3, 4, False) == 2

    assert day_11.count_seats(case_0, 3, 3, True) == 0
    assert day_11.count_seats(case_1, 1, 1, True) == 0
    assert day_11.count_seats(case_2, 3, 4, True) == 8


def test_play():
    """ Test play function """
    assert day_11.play.__wrapped__(area, 4) == 37
    assert day_11.play.__wrapped__(area, 5, True) == 26
