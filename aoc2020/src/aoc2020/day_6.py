""" AOC Day 6 """
import os
from functools import reduce
import click


def parse_input(input_path):
    """Read the input file and split into lines"""
    groups = []
    group = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            if line == "\n":
                groups.append(group)
                group = []
                continue

            group.append(line.strip("\n"))

        groups.append(group)

    return groups


def get_group_answers(group):
    """Get all the answers of the group"""
    answers = set()

    for item in group:
        answers |= set(item)

    return answers


def get_common_group_answers(group):
    """Get all the answers of the group"""
    answers = set(group[0])
    for i in range(1, len(group)):
        answers &= set(group[i])

    return answers


def count_answers(groups, get_answers):
    """Count the answers from all the groups"""
    return sum(map(lambda x: len(get_answers(x)), groups))


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 6 Main """
    groups = parse_input(input_path)

    click.echo(count_answers(groups, get_group_answers))
    click.echo(count_answers(groups, get_common_group_answers))
