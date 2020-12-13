""" Day 7 Unit test """

from aoc2020 import day_7

parsed_input = {
    "light red": {"bright white": 1, "muted yellow": 2},
    "dark orange": {"bright white": 3, "muted yellow": 4},
    "bright white": {"shiny gold": 1},
    "muted yellow": {"faded blue": 9, "shiny gold": 2},
    "shiny gold": {"dark olive": 1, "vibrant plum": 2},
    "dark olive": {"faded blue": 3, "dotted black": 4},
    "vibrant plum": {"faded blue": 5, "dotted black": 6},
    "faded blue": {},
    "dotted black": {},
}

parsed_input_extra = {
    "shiny gold": {"dark red": 2},
    "dark red": {"dark orange": 2},
    "dark orange": {"dark yellow": 2},
    "dark yellow": {"dark green": 2},
    "dark green": {"dark blue": 2},
    "dark blue": {"dark violet": 2},
    "dark violet": {},
}


def test_parse_bag_contents():
    """ Test parse_bag_contents function """
    bag_contents = [
        (
            " 1 bright white bag, 2 muted yellow bags.",
            {"bright white": 1, "muted yellow": 2},
        ),
        (
            "3 bright white bags, 4 muted yellow bags.",
            {"bright white": 3, "muted yellow": 4},
        ),
        (" 1 shiny gold bag.", {"shiny gold": 1}),
        (
            " 2 shiny gold bags, 9 faded blue bags.",
            {"faded blue": 9, "shiny gold": 2},
        ),
        (
            "1 dark olive bag, 2 vibrant plum bags.",
            {"dark olive": 1, "vibrant plum": 2},
        ),
        (
            "3 faded blue bags, 4 dotted black bags.",
            {"faded blue": 3, "dotted black": 4},
        ),
        (
            " 5 faded blue bags, 6 dotted black bags.",
            {"faded blue": 5, "dotted black": 6},
        ),
        (" no other bags.", {}),
        ("no other bags.", {}),
    ]
    for (content, result) in bag_contents:
        assert day_7.parse_bag_contents(content) == result


def test_parse_line():
    """ Test parse_line function """
    bag_contents = [
        (
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            {"light red": {"bright white": 1, "muted yellow": 2}},
        ),
        (
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            {"dark orange": {"bright white": 3, "muted yellow": 4}},
        ),
        (
            "bright white bags contain 1 shiny gold bag.",
            {"bright white": {"shiny gold": 1}},
        ),
        (
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            {"muted yellow": {"faded blue": 9, "shiny gold": 2}},
        ),
        (
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            {"shiny gold": {"dark olive": 1, "vibrant plum": 2}},
        ),
        (
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            {"dark olive": {"faded blue": 3, "dotted black": 4}},
        ),
        (
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            {"vibrant plum": {"faded blue": 5, "dotted black": 6}},
        ),
        ("faded blue bags contain no other bags.", {"faded blue": {}}),
        ("dotted black bags contain no other bags.", {"dotted black": {}}),
    ]
    for (content, result) in bag_contents:
        assert day_7.parse_line(content) == result


def test_parse_input():
    """ Test parse_input function """
    assert day_7.parse_input("./data/day7/test_input.txt") == parsed_input


def test_bag_contains():
    """ Test bag_contains function """
    input_list = [
        ("light red", True),
        ("dark orange", True),
        ("bright white", True),
        ("muted yellow", True),
        ("shiny gold", False),
        ("dark olive", False),
        ("vibrant plum", False),
        ("faded blue", False),
        ("dotted black", False),
    ]

    for (color, result) in input_list:
        assert day_7.bag_contains(parsed_input, color, "shiny gold") == result


def test_count_bags():
    """ Test bag_contains function """
    assert day_7.count_bags(parsed_input, "shiny gold") == 4


def test_count_bags_deep():
    """ Test bag_contains_deep function """
    assert day_7.count_bag_contents(parsed_input, "shiny gold") == 32
    assert day_7.count_bag_contents(parsed_input_extra, "shiny gold") == 126
