""" Day 23: Crab Cups """
import os
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input"""
    with open(os.path.abspath(input_path)) as input_file:
        return input_file.read().strip("\n")


def play(cups, moves):
    """ Play a game of cups """
    size = len(cups)
    circle = [0] * (size + 1)

    for index in range(size - 1):
        circle[cups[index]] = cups[index + 1]
    circle[cups[-1]] = cups[0]

    current = cups[0]

    for _ in range(moves):
        first = circle[current]
        second = circle[first]
        third = circle[second]

        after = circle[third]

        pick_up = [first, second, third]

        destination = current - 1
        while destination in pick_up or destination == 0:
            destination -= 1
            if destination < 1:
                destination = size

        circle[current] = after
        circle[third] = circle[destination]
        circle[destination] = first

        current = after

    return circle


@timer
def part_1(cups):
    """ Solve part 1"""
    circle = play(cups, 100)
    result = ""
    current = circle[1]
    while current != 1:
        result += str(current)
        current = circle[current]

    return result


@timer
def part_2(cups):
    """ Solve part 2 """
    circle = play(cups, 10000000)
    first = circle[1]
    second = circle[first]

    return first * second


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 23 Main """
    cups_input = parse_input(input_path)
    cups = list(map(int, list(cups_input)))

    click.echo("Day 23: Crab Cups")
    click.echo(f"Part 1: {part_1(cups)}")

    cups += list(range(len(cups) + 1, 1000001))
    click.echo(f"Part 2: {part_2(cups)}")
