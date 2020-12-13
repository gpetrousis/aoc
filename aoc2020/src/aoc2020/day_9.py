""" AOC Day 9 """
import os
import click


def parse_input(input_path):
    """Read the input file and parse it into an array of integers"""
    numbers = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            numbers.append(int(line))

    return numbers


def is_sum_of_data(data, total):
    """ Check if a + b == total, Where a, b are items of the data list """
    sorted_data = sorted(data)

    for (i, _) in enumerate(sorted_data):
        for j in range(len(sorted_data) - 1, i, -1):
            sum_data = sorted_data[i] + sorted_data[j]

            if sum_data == total:
                return True

            if sum_data < total:
                break

    return False


def find_invalid_number(data, preamble):
    """Find the first number that there are no
    two numbers in the preamble that sum to it
    """
    for i in range(preamble, len(data)):
        if not is_sum_of_data(data[i - preamble : i], data[i]):
            return data[i]

    return None


def find_weekness(data, invalid):
    """Find a contiguous set of at least two
    numbers that sum up to the invalid number
    """
    for (i, value) in enumerate(data):
        acc = value
        for j in range(i + 1, len(data)):
            acc = acc + data[j]
            if acc == invalid:
                return max(data[i : j + 1]) + min(data[i : j + 1])

            if acc > invalid:
                break

    return None


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.option("--preamble", default=25, help="Preamble number.")
def main(input_path, preamble):
    """ AOC Day 9 Main """
    numbers = parse_input(input_path)
    invalid = find_invalid_number(numbers, preamble)
    click.echo(invalid)
    click.echo(find_weekness(numbers, invalid))
