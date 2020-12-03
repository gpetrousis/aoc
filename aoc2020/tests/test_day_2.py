""" Day 2 Unit test """

# import click.testing
from aoc2020 import day_2

data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

def test_parse_input():
    """ Test parse_input function """
    assert day_2.parse_input('./data/day2/test_input.txt') == data

def test_parse_line():
    """ Test parse_line function """
    assert day_2.parse_line(data[0]) == ["1-3 a", "abcde"]

def test_parse_policy():
    """ Test parse_policy function """
    [policy, _] = day_2.parse_line(data[0])
    assert day_2.parse_policy(policy) == [1, 3, "a"]

def test_is_valid_limits():
    """ Test is_valit_limits function """
    [policy, password] = day_2.parse_line(data[0])
    assert day_2.is_valid_limits(policy, password)

    [policy, password] = day_2.parse_line(data[1])
    assert not day_2.is_valid_limits(policy, password)

    [policy, password] = day_2.parse_line(data[2])
    assert day_2.is_valid_limits(policy, password)

def test_is_valid_possition():
    """ Test is_valid_possition function """
    [policy, password] = day_2.parse_line(data[0])
    assert day_2.is_valid_possition(policy, password)

    [policy, password] = day_2.parse_line(data[1])
    assert not day_2.is_valid_possition(policy, password)

    [policy, password] = day_2.parse_line(data[2])
    assert not day_2.is_valid_possition(policy, password)

def test_count_valid_passwords():
    """ Test count_valid_passwords """
    assert day_2.count_valid_passwords(data, day_2.is_valid_limits) == 2
    assert day_2.count_valid_passwords(data, day_2.is_valid_possition) == 1
