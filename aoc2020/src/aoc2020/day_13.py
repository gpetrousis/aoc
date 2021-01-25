""" Day 13: Shuttle Search
The solution is based on
https://rosettacode.org/wiki/Chinese_remainder_theorem
"""

import os
from functools import reduce
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Read the input file and parse it into a 2d array"""
    timestamp = 0
    busses = []
    with open(os.path.abspath(input_path)) as input_file:
        lines = list(input_file)

    timestamp = int(lines[0].rstrip("\n"))
    for (index, bus) in enumerate(lines[1].rstrip("\n").split(",")):
        if bus == "x":
            continue

        busses.append((int(bus), index))

    return (timestamp, busses)


@timer
def find_next_bus(arrival, busses):
    """Find the next departing bus affter the arrival time"""
    next_bus = (None, None)

    for (bus, _) in busses:
        departs_in = bus - arrival % bus
        if next_bus == (None, None) or departs_in < next_bus[1]:
            next_bus = (bus, departs_in)

    return next_bus[0] * next_bus[1]


@timer
def chinese_remainder(busses):
    """Apply the chinese remainder theorem for the busses and their ids
    busses = [(bus_id, index)...]
    """
    acc = 0
    busses_numbers = map(lambda a: a[0], busses)
    product = reduce(lambda a, b: a * b, busses_numbers)

    for (num_i, index_i) in busses:
        rem_i = -index_i % num_i
        p = product // num_i
        acc += rem_i * p * multiplicative_inverse(p, num_i)

    return acc % product


def multiplicative_inverse(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 13 Main """
    (arrival, busses) = parse_input(input_path)

    click.echo("Day 13: Shuttle Search")
    click.echo(f"Part 1: {find_next_bus(arrival, busses)}")
    click.echo(f"Part 2: {chinese_remainder(busses)}")
