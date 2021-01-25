""" Day 19: Monster Messages
The solution is based on
https://github.com/mebeim/aoc/blob/master/2020/solutions/day19.py
Big kudos to Membeim!
"""

import os
from copy import deepcopy
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input"""
    rules_raw = []
    messages = []

    rules = {}

    with open(os.path.abspath(input_path)) as input_file:
        lines = list(input_file)
        for (index, line) in enumerate(lines):
            if line == "\n":
                rules_raw = [x.rstrip("\n") for x in lines[:index]]
                messages = [x.rstrip("\n") for x in lines[index + 1 :]]
                break

    for rule in rules_raw:
        # id: 1 2 3 | 3 2 1
        [index, expression] = [x.strip() for x in rule.split(":")]
        index = int(index)
        if '"' in expression:
            rules[index] = expression.strip('"')
        else:
            rules[index] = []
            parts = [x.strip() for x in expression.split("|")]
            for part in parts:
                rules[index].append([int(x) for x in part.split(" ")])

    return (rules, messages)


def match(rules, string, rule=0, index=0):
    """ Check if the string is matching a rules """
    if index == len(string):
        return []

    rule = rules[rule]
    if isinstance(rule, str):
        if string[index] == rule:
            return [index + 1]
        return []

    matches = []
    for option in rule:
        sub_matches = [index]

        for sub_rule in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += match(rules, string, sub_rule, idx)
            sub_matches = new_matches

        matches += sub_matches

    return matches


@timer
def count_matched_rules(rules, messages):
    """ Count all the messages that match rule 0 """
    matched = 0
    for msg in messages:
        if len(msg) in match(rules, msg):
            matched += 1

    return matched


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 19 Main """
    (rules, messages) = parse_input(input_path)

    rules_2 = deepcopy(rules)
    rules_2[8] = [[42], [42, 8]]
    rules_2[11] = [[42, 31], [42, 11, 31]]

    click.echo("Day 19: Monster Messages")
    click.echo(f"Part 1: {count_matched_rules(rules, messages)}")
    click.echo(f"Part 2: {count_matched_rules(rules_2, messages)}")
