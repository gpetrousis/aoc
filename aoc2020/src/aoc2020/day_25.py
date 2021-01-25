""" Day 25: Combo Breaker """
import os
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input"""
    with open(os.path.abspath(input_path)) as input_file:
        return [int(key.strip()) for key in input_file]


def transform(seed, subject_num, loop):
    """ Transform a subject number """
    key = seed

    for _ in range(loop):
        key *= subject_num
        key = key % 20201227

    return key


def find_loop(key):
    """ Find the loop size of the key """
    loop = 0
    seed = 1
    while seed != key:
        seed = transform(seed, 7, 1)
        loop += 1

    return loop


@timer
def find_encryption_key(card_pub, door_pub):
    """ Find the encryption key """
    card_loop = find_loop(card_pub)
    return transform(1, door_pub, card_loop)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 25 Main """
    [card_pub, door_pub] = parse_input(input_path)

    click.echo("Day 25: Combo Breaker")
    click.echo(f"Part 1: {find_encryption_key(card_pub, door_pub)}")
