""" AOC Day 10 """
import os
import click


def parse_input(input_path):
    """Read the input file and parse it into an array of integers"""
    numbers = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            numbers.append(int(line.rstrip("\n")))

    return numbers


def get_joltage_difference(jolts):
    """Return the product of the 1-jolt and 3-jolt differences"""
    sorted_jolts = sorted(jolts)
    sorted_jolts.insert(0, 0)  # Add the first jolt of the wall plug
    sorted_jolts.append(sorted_jolts[-1] + 3)  # Add the last jolt of the laptop plug

    diffs = [0, 0, 0]
    for i in range(0, len(sorted_jolts) - 1):
        jolt_diff = sorted_jolts[i + 1] - sorted_jolts[i] - 1

        if jolt_diff > 2:
            click.echo("Jolt difference too big")
            return None

        diffs[jolt_diff] = diffs[jolt_diff] + 1

    return diffs[0] * diffs[2]


def get_joltage_arrangements(jolts):
    """Return the number of distinct arrangements"""
    sorted_jolts = sorted(jolts)
    sorted_jolts.append(sorted_jolts[-1] + 3)  # Add the last jolt of the laptop plug

    memoization = {0: 1}

    for jolt in sorted_jolts:
        memoization[jolt] = (
            memoization.get(jolt - 3, 0)
            + memoization.get(jolt - 2, 0)
            + memoization.get(jolt - 1, 0)
        )

    return memoization[sorted_jolts[-1]]


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 10 Main """
    jolts = parse_input(input_path)
    click.echo(get_joltage_difference(jolts))
    click.echo(get_joltage_arrangements(jolts))

