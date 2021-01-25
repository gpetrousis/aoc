""" Day 2: Password Philosophy """
import os
import re
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """ Read the input file and split into lines """
    with open(os.path.abspath(input_path)) as input_file:
        input_data = [line.rstrip("\n") for line in input_file]

    return input_data


def parse_line(line):
    """
    Parse a line and return the components based on the pattern
    <policy>: <password>
    """
    return [s.strip() for s in line.split(":")]


def parse_policy(policy):
    """
    Parse a line and return the components based on the pattern
    <policy>: <password>
    """
    pattern = re.compile(r"^(\d+)-(\d+)\s(\w)$")
    match = pattern.match(policy)
    if match is not None:
        return [int(match.group(1)), int(match.group(2)), match.group(3)]


def is_within_limits(policy, password):
    """
    Validate if a password is valid based on the
    policy low_limit <= count(letter) <= high_limit
    """
    [low, high, letter] = parse_policy(policy)

    count = password.count(letter)

    return low <= count <= high


def is_valid_possition(policy, password):
    """
    Validate if a password is valid based on the
    policy that the letter exist on only one of
    the positions provided in the policy
    """
    [pos1, pos2, letter] = parse_policy(policy)

    exist_pos1 = password[pos1 - 1] == letter
    exist_pos2 = password[pos2 - 1] == letter

    return exist_pos1 != exist_pos2


@timer
def count_valid_passwords(password_list, validator):
    """
    Count how many valid passwords exist in the input
    list based on the provided validator function
    """
    count = 0
    for line in password_list:
        [policy, password] = parse_line(line)
        if validator(policy, password):
            count += 1

    return count


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ Main function """
    input_data = parse_input(input_path)

    click.echo("Day 2: Password Philosophy")
    click.echo(f"Part 1: {count_valid_passwords(input_data, is_within_limits)}")
    click.echo(f"Part 2: {count_valid_passwords(input_data, is_valid_possition)}")
