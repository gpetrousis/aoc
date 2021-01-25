""" Day 16 Unit test """

from aoc2020 import day_16

raw_rules = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50"
]


data = {
    "rules": [
        ("class", [(1, 3), (5, 7)]),
        ("row", [(6, 11), (33, 44)]),
        ("seat", [(13, 40), (45, 50)]),
    ],
    "my_ticket": [7, 1, 14],
    "nearby_tickets": [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]],
}


data_part_2 = {
    "rules": [
        ("class", [(0, 1), (4, 19)]),
        ("row", [(0, 5), (8, 19)]),
        ("seat", [(0, 13), (16, 19)]),
    ],
    "my_ticket": [11, 12, 13],
    "nearby_tickets": [[3, 9, 18], [15, 1, 5], [5, 14, 9]]
}


def test_parse_rule():
    """ Test parse_rule function """
    assert day_16.parse_rule(raw_rules[0]) == data["rules"][0]
    assert day_16.parse_rule(raw_rules[1]) == data["rules"][1]
    assert day_16.parse_rule(raw_rules[2]) == data["rules"][2]


def test_parse_input():
    """ Test parse_input function """
    assert day_16.parse_input("./data/day16/test_input.txt") == data


def test_is_invalid_for_all_rules():
    """ Test is_invalid_for_all_rules function """
    assert day_16.is_invalid_for_all_rules(data["nearby_tickets"][1][1], data["rules"])
    assert day_16.is_invalid_for_all_rules(data["nearby_tickets"][2][0], data["rules"])
    assert day_16.is_invalid_for_all_rules(data["nearby_tickets"][3][2], data["rules"])

    assert not day_16.is_invalid_for_all_rules(data["nearby_tickets"][1][0], data["rules"])
    assert not day_16.is_invalid_for_all_rules(data["nearby_tickets"][2][2], data["rules"])
    assert not day_16.is_invalid_for_all_rules(data["nearby_tickets"][3][1], data["rules"])


def test_is_valid_field():
    """ Test is_valid_field function """
    assert not day_16.is_valid_field(data_part_2["nearby_tickets"][0][0], data_part_2["rules"][0][1])
    assert day_16.is_valid_field(data_part_2["nearby_tickets"][0][1], data_part_2["rules"][0][1])
    assert day_16.is_valid_field(data_part_2["nearby_tickets"][0][0], data_part_2["rules"][1][1])


def test_count_invalid_fields():
    """ Test count_invalid_fields function """
    assert day_16.count_invalid_fields.__wrapped__(data["nearby_tickets"], data["rules"]) == 71


def test_resolve_possible_indexes():
    """ Test resolve_possible_indexes function """
