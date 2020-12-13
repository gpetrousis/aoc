""" AOC Day 4 """
import os
import click


def parse_input(input_path):
    """Read the input file and split into lines"""
    with open(os.path.abspath(input_path)) as input_file:
        input_data = [line.rstrip("\n") for line in input_file]

    return input_data


def parse_code(code, low, high):
    """Parse seat code"""
    if code == "":
        return low
    if code[0] == "F" or code[0] == "L":
        return parse_code(code[1:], low, low + int((high - low) / 2))

    if code[0] == "B" or code[0] == "R":
        return parse_code(code[1:], low + int((high - low) / 2) + 1, high)


def parse_code_binary(code):
    """Parse seat code"""
    binary = ""
    for letter in code:
        if letter == "F" or letter == "L":
            binary += "0"

        if letter == "B" or letter == "R":
            binary += "1"

    return int(binary, 2)


def parse_seat(seat):
    """Parse seat into row and column"""
    row = parse_code_binary(seat[:7])
    column = parse_code_binary(seat[7:])

    return [row, column]


def get_seat_id(seat):
    """Get the seat id"""
    [row, column] = parse_seat(seat)

    return row * 8 + column


def get_max_seat_id(seats):
    """Get the max seat id"""
    return max(map(lambda x: get_seat_id(x), seats))


def find_my_seat(seats):
    """Find the missing seat"""
    seat_ids = map(lambda x: get_seat_id(x), seats)
    sorted_seats = sorted(seat_ids)

    for i in range(len(sorted_seats)):
        if sorted_seats[i + 1] == sorted_seats[i] + 2:
            return sorted_seats[i] + 1

    return -1


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 5 Main """
    seats = parse_input(input_path)

    click.echo(get_max_seat_id(seats))
    click.echo(find_my_seat(seats))
