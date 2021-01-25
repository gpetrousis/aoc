""" Day 12: Rain Risk """
import os
import re
import click
from aoc2020.timer import timer

DIRECTIONS = ["E", "S", "W", "N"]


def parse_input(input_path):
    """Read the input file and parse it into a 2d array"""
    steps = []
    pattern = re.compile(r"^([A-Z])(\d*)$")
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            match = re.match(pattern, line)
            steps.append((match.group(1), int(match.group(2))))

    return steps


def turn(direction_index, direction, degrees):
    """Turn the direction depending to where it should turn and the degrees"""
    diff = degrees // 90
    if direction == "R":
        return (direction_index + diff) % 4

    if direction == "L":
        return (direction_index - diff) % 4

    return None


def rotate(x, y, direction, degrees):
    """Rotate the direction depending to where it should turn and the degrees"""
    diff = degrees // 90
    if direction == "R":
        for _ in range(diff):
            (x, y) = (y, -x)
        return (x, y)

    if direction == "L":
        for _ in range(diff):
            (x, y) = (-y, x)
        return (x, y)

    return None


def step(direction, steps):
    """Return the number of steps toward the given direction"""
    if direction == "E":
        return (steps, 0)

    if direction == "S":
        return (0, -steps)

    if direction == "W":
        return (-steps, 0)

    if direction == "N":
        return (0, steps)

    return None


def manhatan(start_x, start_y, end_x, end_y):
    """Return the manhatan distance of two points"""
    return abs(start_x - end_x) + abs(start_y - end_y)


@timer
def move_ship(instructions):
    """Apply the instructions on the ship"""
    ship_x = 0
    ship_y = 0
    direction_index = 0

    for instruction in instructions:
        (key, value) = instruction

        if key == "F":
            (step_x, step_y) = step(DIRECTIONS[direction_index], value)
            ship_x += step_x
            ship_y += step_y

        if key in DIRECTIONS:
            (step_x, step_y) = step(key, value)
            ship_x += step_x
            ship_y += step_y

        if key in ["L", "R"]:
            direction_index = turn(direction_index, key, value)

    return manhatan(0, 0, ship_x, ship_y)


@timer
def move_waypoint(instructions):
    """Apply the instructions on the ship and waypoint"""
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1

    for instruction in instructions:
        (key, value) = instruction

        if key == "F":
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value
            continue

        if key in DIRECTIONS:
            (step_x, step_y) = step(key, value)
            waypoint_x += step_x
            waypoint_y += step_y
            continue

        if key in ["L", "R"]:
            (waypoint_x, waypoint_y) = rotate(waypoint_x, waypoint_y, key, value)

    return manhatan(0, 0, ship_x, ship_y)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 12 Main """
    instructions = parse_input(input_path)

    click.echo("Day 12: Rain Risk")
    click.echo(f"Part 1: {move_ship(instructions)}")
    click.echo(f"Part 2: {move_waypoint(instructions)}")
