""" Day 4 Unit test """

# import click.testing
from aoc2020 import day_4

data = [
    {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    },
    {
        "iyr": "2013",
        "ecl": "amb",
        "cid": "350",
        "eyr": "2023",
        "pid": "028048884",
        "hcl": "#cfa07d",
        "byr": "1929",
    },
    {
        "hcl": "#ae17e1",
        "iyr": "2013",
        "eyr": "2024",
        "ecl": "brn",
        "pid": "760753108",
        "byr": "1931",
        "hgt": "179cm",
    },
    {
        "hcl": "#cfa07d",
        "eyr": "2025",
        "pid": "166559648",
        "iyr": "2011",
        "ecl": "brn",
        "hgt": "59in",
    },
]

invalid_passports = [
    {
        "eyr": "1972",
        "cid": "100",
        "hcl": "#18171d",
        "ecl": "amb",
        "hgt": "170",
        "pid": "186cm",
        "iyr": "2018",
        "byr": "1926",
    },
    {
        "iyr": "2019",
        "hcl": "#602927",
        "eyr": "1967",
        "hgt": "170cm",
        "ecl": "grn",
        "pid": "012533040",
        "byr": "1946",
    },
    {
        "hcl": "dab227",
        "iyr": "2012",
        "ecl": "brn",
        "hgt": "182cm",
        "pid": "021572410",
        "eyr": "2020",
        "byr": "1992",
        "cid": "277",
    },
    {
        "hgt": "59cm",
        "ecl": "zzz",
        "eyr": "2038",
        "hcl": "74454a",
        "iyr": "2023",
        "pid": "3556412378",
        "byr": "2007",
    },
]

valid_passports = [
    {
        "pid": "087499704",
        "hgt": "74in",
        "ecl": "grn",
        "iyr": "2012",
        "eyr": "2030",
        "byr": "1980",
        "hcl": "#623a2f",
    },
    {
        "eyr": "2029",
        "ecl": "blu",
        "cid": "129",
        "byr": "1989",
        "iyr": "2014",
        "pid": "896056539",
        "hcl": "#a97842",
        "hgt": "165cm",
    },
    {
        "hcl": "#888785",
        "hgt": "164cm",
        "byr": "2001",
        "iyr": "2015",
        "cid": "88",
        "pid": "545766238",
        "ecl": "hzl",
        "eyr": "2022",
    },
    {
        "iyr": "2010",
        "hgt": "158cm",
        "hcl": "#b6652a",
        "ecl": "blu",
        "byr": "1944",
        "eyr": "2021",
        "pid": "093154719",
    },
]


def test_parse_input():
    """ Test parse_input function """
    assert day_4.parse_input("./data/day4/test_input.txt") == data


def test_is_valid_passport():
    """ Test is_valis_passport function """
    assert day_4.is_valid_passport(data[0])
    assert not day_4.is_valid_passport(data[1])
    assert day_4.is_valid_passport(data[2])
    assert not day_4.is_valid_passport(data[3])


def test_count_valid_passports():
    """ Test count_valid_passports function """
    assert day_4.count_valid_passports(data, day_4.is_valid_passport) == 2


def test_validators():
    """ Test test validators function """
    test_input = [
        [{"byr": "2002"}, True],
        [{"byr": "2003"}, False],
        [{"hgt": "60in"}, True],
        [{"hgt": "190cm"}, True],
        [{"hgt": "190in"}, False],
        [{"hgt": "190"}, False],
        [{"hcl": "#123abc"}, True],
        [{"hcl": "#123abz"}, False],
        [{"hcl": "123abc"}, False],
        [{"ecl": "brn"}, True],
        [{"ecl": "wat"}, False],
        [{"pid": "000000001"}, True],
        [{"pid": "0123456789"}, False],
    ]

    for [item, result] in test_input:
        for key in item:
            assert day_4.validators[key](item[key]) == result


def test_is_valid_passport_strict():
    """ Test is_valis_passport function """
    for passport in invalid_passports:
        assert not day_4.is_valid_passport_strict(passport)

    for passport in valid_passports:
        assert day_4.is_valid_passport_strict(passport)
