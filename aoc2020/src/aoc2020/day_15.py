""" Day 15: Rambunctious Recitation """
import os
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input"""
    with open(os.path.abspath(input_path)) as input_file:
        lines = list(input_file)
        return list(map(int, lines[0].split(",")))


@timer
def find_number(seed, end):
    """Find the <end>th number"""
    seen = dict()
    turn = 1
    next_num = 0

    for num in seed:
        seen[num] = turn
        turn += 1

    while turn < end:
        last_index = seen.get(next_num, 0)
        if last_index == 0:
            seen[next_num] = turn
            next_num = 0
        else:
            seen[next_num] = turn
            next_num = turn - last_index

        turn += 1

    return next_num


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 15 Main """
    seed = parse_input(input_path)

    click.echo("Day 15: Rambunctious Recitation")
    click.echo(f"Part 1: {find_number(seed, 2020)}")
    click.echo(f"Part 2: {find_number(seed, 30000000)}")
