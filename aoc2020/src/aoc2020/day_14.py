""" Day 14: Docking Data """
import os
import re
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input"""
    instructions = []
    pattern = re.compile(r"^mem\[(\d*)\]$")
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            parts = line.split("=")
            parts = list(map(lambda x: x.strip(), parts))

            if parts[0] == "mask":
                instructions.append((parts[0], parts[1]))
                continue

            match = re.match(pattern, parts[0])
            instructions.append((int(match.group(1)), int(parts[1])))

    return instructions


def apply_mask(binary, mask):
    """Apply a mask on a binary number"""
    binary_list = list(binary)
    for (index, digit) in enumerate(mask):
        if digit == "X":
            continue

        binary_list[index] = digit

    return "".join(binary_list)


def apply_char(string, char, index):
    """Change the char on the given index of the string"""
    str_list = list(string)
    str_list[index] = char
    return "".join(map(str, str_list))


def apply_mask_v2(binary, mask):
    """Apply mask Version 2"""
    binary_list = list(binary)
    mask_list = list(mask)

    for (index, digit) in enumerate(mask_list):
        if digit == "0":
            continue

        binary_list[index] = digit

    return "".join(binary_list)


def decimal_to_binary(num):
    """Convert a decimal int to a binary string of 36 bits"""
    return "{0:036b}".format(num)


def sum_mem(mem):
    """Sum mem into a dec"""
    return sum(map(lambda x: int(x, 2), mem.values()))


def resolve_masked_address(address):
    """Resolve Xs in an address to 0 & 1 digits"""
    if "X" not in address:
        return [address]

    index = address.find("X")
    return resolve_masked_address(
        address[:index] + "0" + address[index + 1 :]
    ) + resolve_masked_address(address[:index] + "1" + address[index + 1 :])


@timer
def initialize_program(instructions):
    """Run program initialization"""
    mask = ""
    mem = dict()

    for (key, value) in instructions:
        if key == "mask":
            mask = value
            continue

        binary = decimal_to_binary(value)
        mem[key] = apply_mask(binary, mask)

    return sum_mem(mem)


@timer
def initialize_program_v2(instructions):
    """Run program initialization Version 2"""
    mask = ""
    mem = dict()

    for (key, value) in instructions:
        if key == "mask":
            mask = value
            continue

        binary = decimal_to_binary(key)

        masked_address = apply_mask_v2(binary, mask)
        addresses = resolve_masked_address(masked_address)

        for address in addresses:
            mem[address] = value

    return sum(mem.values())


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 14 Main """
    instructions = parse_input(input_path)

    click.echo("Day 14: Docking Data")
    click.echo(f"Part 1: {initialize_program(instructions)}")
    click.echo(f"Part 2: {initialize_program_v2(instructions)}")
