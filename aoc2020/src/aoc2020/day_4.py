""" AOC Day 4 """
import os
import re
from functools import reduce
import click


def is_valid_height(height):
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
    "byr": lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
    "hgt": is_valid_height,
    "hcl": lambda x: re.search(r"^#[0-9,a-f]{6}$", x) is not None,
    "ecl": lambda x: re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", x) is not None,
    "pid": lambda x: re.search(r"^\d{9}$", x) is not None,
    "cid": lambda x: True
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
        if not key in passport or not validators[key](passport[key]):
            return False

    return True


def count_valid_passports(passports, validator):
    """Count all the valid passports"""
    count = 0
    for passport in passports:
        if validator(passport):
            count = count + 1

    return count


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 3 Main """
    passports = parse_input(input_path)

    click.echo(count_valid_passports(passports, is_valid_passport))
    click.echo(count_valid_passports(passports, is_valid_passport_strict))
