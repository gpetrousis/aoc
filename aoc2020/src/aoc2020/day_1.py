""" AOC Day 1 """
import os
import click


def get_sum_two(data, total):
    """ Return a * b if a + b == total, Where a, b are items of the data list """
    for i in range(0, len(data)):
        for j in range(len(data) - 1, i + 1, -1):
            sum_data = data[i] + data[j]

            if sum_data == total:
                return data[i] * data[j]

            if sum_data < total:
                break

    return "Sum not found"


def get_sum_three(data, total):
    """
    Return a * b * c if a + b + c == total,
    where a, b, c are items of the data list
    """
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                sum_data = data[i] + data[j] + data[k]

                if sum_data == total:
                    return data[i] * data[j] * data[k]

                if sum_data > total:
                    break

    return "Sum not found"


def parse_input(input_path):
    """ Parse the input file into an array of integers """
    with open(os.path.abspath(input_path)) as input_file:
        input_data = list(input_file)

    return [int(i) for i in input_data]


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 1 Main """
    data = parse_input(input_path)

    sorted_data = sorted(data)

    click.echo(get_sum_two(sorted_data, 2020))
    click.echo(get_sum_three(sorted_data, 2020))
