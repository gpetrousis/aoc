""" Day 8: Handheld Halting """
import os
import copy
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Read the input file and add the commands into an array of (opperator, value)"""
    commands = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            parts = line.rstrip("\n").split(" ")
            commands.append((parts[0], int(parts[1])))

    return commands


def run_commands(commands):
    """Run the given commands and return if the
    execution was successful and the accumulator
    """
    acc = 0
    index = 0

    executed_commands = set()

    done = True
    while index < len(commands):
        if index in executed_commands:
            done = False
            break

        executed_commands.add(index)
        (opperator, argument) = commands[index]
        if opperator == "nop":
            index += 1

        elif opperator == "acc":
            acc += argument
            index += 1

        elif opperator == "jmp":
            index += argument

    return (done, acc)


def fix_commands(commands):
    """Iterate over the commands and try to fix the code"""
    for (index, command) in enumerate(commands):
        (opperator, value) = command
        commands_copy = copy.copy(commands)
        if opperator == "acc":
            continue

        if opperator == "nop":
            commands_copy[index] = ("jmp", value)

        elif opperator == "jmp":
            commands_copy[index] = ("nop", value)

        (success, result) = run_commands(commands_copy)

        if success:
            return result

    return None


@timer
def part_1(commands):
    """ Solve part 1 """
    (_, result) = run_commands(commands)
    return result


@timer
def part_2(commands):
    """ Solve part 2 """
    return fix_commands(commands)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 8 Main """
    commands = parse_input(input_path)

    click.echo("Day 8: Handheld Halting")
    click.echo(f"Part 1: {part_1(commands)}")
    click.echo(f"Part 2: {part_2(commands)}")
