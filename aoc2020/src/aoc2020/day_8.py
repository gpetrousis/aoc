""" AOC Day 8 """
import os
import copy
import click


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
            index = index + 1

        elif opperator == "acc":
            acc = acc + argument
            index = index + 1

        elif opperator == "jmp":
            index = index + argument

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


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 8 Main """
    commands = parse_input(input_path)
    click.echo(run_commands(commands))
    click.echo(fix_commands(commands))
