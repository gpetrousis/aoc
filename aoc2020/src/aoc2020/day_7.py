""" AOC Day 7 """
import os
import re
import click


def parse_bag_contents(contents):
    """Parse the contents of a bag into a dict eg: {'bright white': '1'}"""
    bags = {}
    if contents == "no bags":
        return bags

    pattern = re.compile(r"\s?(\d)\s(.*)\sbags?")
    for content in contents.split(","):
        match = re.match(pattern, content)

        if not match:
            continue

        bags[match.group(2)] = int(match.group(1))

    return bags


def parse_line(line):
    """Parse input line into {'bag color': {'content bag': count}} dict"""
    pattern = re.compile(r"^(.*)\sbags?\scontain\s(.*).$")
    match = re.match(pattern, line)

    if not match:
        return None

    return {match.group(1): parse_bag_contents(match.group(2))}


def parse_input(input_path):
    """Read the input file and split into bag objects"""
    bags = dict()
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            bags = {**bags, **parse_line(line)}

    return bags


def bag_contains(bags, parent, color):
    """Search if a bag can contains another bag of a specific color"""
    contents = bags.get(parent, {})

    if contents == {}:
        return False

    keys = contents.keys()

    for key in keys:
        if color == key or bag_contains(bags, key, color):
            return True

    return False


def count_bag_contents(bags, parent):
    """Count all the bags contained in the parent bag"""
    contents = bags.get(parent, {})

    if contents == {}:
        return 0

    count = 0
    keys = contents.keys()
    for key in keys:
        key_count = contents[key]
        result = count_bag_contents(bags, key)
        count = count + key_count + (key_count * result)

    return count


def count_bags(bags, color):
    """Count all the bags that contain the color"""
    count = 0
    for parent in bags.keys():
        if bag_contains(bags, parent, color):
            count += 1

    return count


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 7 Main """
    bags = parse_input(input_path)
    click.echo(count_bags(bags, "shiny gold"))
    click.echo(count_bag_contents(bags, "shiny gold"))
