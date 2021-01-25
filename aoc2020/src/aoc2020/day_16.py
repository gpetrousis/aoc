"""
Day 16: Ticket Translation
"""
import os
import re
from copy import copy
import click
from aoc2020.timer import timer


def parse_rule(rule):
    """Parse the rule into (name, [bundaries])"""
    pattern = re.compile(r"^(.*): (\d*)-(\d*) or (\d*)-(\d*)$")
    match = re.match(pattern, rule)

    return (
        match.group(1),
        [
            (int(match.group(2)), int(match.group(3))),
            (int(match.group(4)), int(match.group(5))),
        ],
    )


def parse_input(input_path):
    """Parse the input"""
    part = "rules"
    rules = []
    my_ticket = []
    nearby_tickets = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            if line == "\n":
                continue

            if line == "your ticket:\n":
                part = "your ticket"
                continue

            if line == "nearby tickets:\n":
                part = "nearby tickets"
                continue

            if part == "rules":
                rules.append(parse_rule(line))

            elif part == "your ticket":
                my_ticket = list(map(int, line.rstrip("\n").split(",")))

            else:
                nearby_tickets.append(list(map(int, line.rstrip("\n").split(","))))

    return {"rules": rules, "my_ticket": my_ticket, "nearby_tickets": nearby_tickets}


def is_invalid_for_all_rules(field, rules):
    """Check if a field is invalid for all the giver rules"""
    for (_, boundaries) in rules:
        if is_valid_field(field, boundaries):
            return False

    return True


def is_valid_field(field, rule):
    """Check if the field is valid for the given rule"""
    for boundary in rule:
        low = boundary[0]
        high = boundary[1]
        if low <= field <= high:
            return True

    return False


@timer
def count_invalid_fields(tickets, rules):
    """Count all the invalid fields"""
    acc = 0

    for ticket in tickets:
        for field in ticket:
            if is_invalid_for_all_rules(field, rules):
                acc += field

    return acc


def is_valid_ticket(ticket, rules):
    """Check if all of the fields of the ticket are valid based on at least one rule"""
    for field in ticket:
        if is_invalid_for_all_rules(field, rules):
            return False

    return True


def resolve_possible_indexes(possible_indexes):
    """Given a set of possible indexes, resolve to 1-to-1 match of rule and index"""
    rules = copy(possible_indexes)
    done = False
    while not done:
        done = True
        for (index, rule_set) in enumerate(rules):
            if len(rule_set) == 1:
                # Remove the possible rules from all other rule sets
                for (i, rule_set_tmp) in enumerate(rules):
                    if i != index:
                        rule_set_tmp -= rules[index]
            else:
                done = False

    return rules


def eliminate_indexes(tickets, rules):
    """Return a list of sets containing possible field indexes per rule"""
    rule_indexes = range(len(rules))
    possible_indexes = []

    for _ in rule_indexes:
        possible_indexes.append(set(rule_indexes))

    for ticket in tickets:
        for (rule_index, (_, boundaries)) in enumerate(rules):
            for (field_index, field) in enumerate(ticket):
                if not is_valid_field(field, boundaries):
                    possible_indexes[rule_index].discard(field_index)

    return possible_indexes


def get_fields(nearby_tickets, my_ticket, rules):
    """ Get fields that start with departure """
    tickets = list(filter(lambda x: is_valid_ticket(x, rules), nearby_tickets))

    possible_indexes = eliminate_indexes(tickets, rules)
    rules_indexes = resolve_possible_indexes(possible_indexes)

    mult = 1
    for (index, (rule_name, _)) in enumerate(rules):
        if rule_name.startswith("departure"):
            field_index = rules_indexes[index].pop()
            mult *= my_ticket[field_index]

    return mult


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 16 Main """
    data = parse_input(input_path)
    nearby_tickets = data["nearby_tickets"]
    rules = data["rules"]
    my_ticket = data["my_ticket"]

    click.echo("Day 16: Ticket Translation")
    click.echo(count_invalid_fields(nearby_tickets, rules))
    click.echo(get_fields(nearby_tickets, my_ticket, rules))
