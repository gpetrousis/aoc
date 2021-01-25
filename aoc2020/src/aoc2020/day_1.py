""" Day 1: Report Repair """
import os
import click
from aoc2020.timer import timer


@timer
def get_sum_two(data, total):
    """ Return a * b if a + b == total, Where a, b are items of the data list """
    sorted_data = sorted(data)
    for (i, _) in enumerate(sorted_data):
        for j in range(len(sorted_data) - 1, i, -1):
            sum_data = sorted_data[i] + sorted_data[j]

            if sum_data == total:
                return sorted_data[i] * sorted_data[j]

            if sum_data < total:
                break

    return None


@timer
def get_sum_three(data, total):
    """
    Return a * b * c if a + b + c == total,
    where a, b, c are items of the data list
    """
    sorted_data = sorted(data)
    for (i, _) in enumerate(sorted_data):
        for j in range(i + 1, len(sorted_data)):
            for k in range(j + 1, len(sorted_data)):
                sum_data = sorted_data[i] + sorted_data[j] + sorted_data[k]

                if sum_data == total:
                    return sorted_data[i] * sorted_data[j] * sorted_data[k]

                if sum_data > total:
                    break

    return None


def parse_input(input_path):
    """ Parse the input file into an array of integers """
    with open(os.path.abspath(input_path)) as input_file:
        input_data = list(input_file)

    return [int(i) for i in input_data]


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ Main Function"""
    data = parse_input(input_path)

    click.echo("Day 1: Report Repair")
    click.echo(f"Part 1: {get_sum_two(data, 2020)}")
    click.echo(f"Part 2: {get_sum_three(data, 2020)}")
