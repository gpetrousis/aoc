""" Day 4: Passport Processing """
import os
import re
import click
from aoc2020.timer import timer


def is_valid_height(height):
    """ Check if the height is within limits """
    pattern = re.compile(r"^(\d*)(cm|in)$")
    match = re.match(pattern, height)
    if not match:
        return False

    value = int(match.group(1))
    if match.group(2) == "cm":
        return value >= 150 and value <= 193

    if match.group(2) == "in":
        return value >= 59 and value <= 76

    return False


valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

validators = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": is_valid_height,
    "hcl": lambda x: re.search(r"^#[0-9,a-f]{6}$", x) is not None,
    "ecl": lambda x: re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x) is not None,
    "pid": lambda x: re.search(r"^\d{9}$", x) is not None,
}


def parse_input(input_path):
    """ Parse the input into a 2D array """
    passports = []
    entry = dict()

    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            if line == "\n":
                passports.append(entry)
                entry = dict()
                continue

            fields = re.split(r"\s", line.strip("\n"))
            for field in fields:
                [key, value] = field.split(":")
                entry[key] = value

        passports.append(entry)

    return passports


def is_valid_passport(passport):
    """Check if all the necessary fields of the passport exist"""
    return all(key in passport for key in valid_fields)


def is_valid_passport_strict(passport):
    """Check if all the necessary fields of the passport exist and are valid"""
    for key in valid_fields:
        if key not in passport or not validators[key](passport[key]):
            return False

    return True


@timer
def count_valid_passports(passports, validator):
    """Count all the valid passports"""
    count = 0
    for passport in passports:
        if validator(passport):
            count += 1

    return count


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ Main Function """
    passports = parse_input(input_path)

    click.echo("Day 4: Passport Processing")
    click.echo(f"Part 1: {count_valid_passports(passports, is_valid_passport)}")
    click.echo(f"Part 2: {count_valid_passports(passports, is_valid_passport_strict)}")
