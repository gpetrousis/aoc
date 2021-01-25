""" Day 14 Unit test """

from aoc2020 import day_14

instructions = [
    ("mask", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"),
    (8, 11),
    (7, 101),
    (8, 0),
]

instructions_v2 = [
    ("mask", "000000000000000000000000000000X1001X"),
    (42, 100),
    ("mask", "00000000000000000000000000000000X0XX"),
    (26, 1),
]

MASK = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"

mem = {
    8: "000000000000000000000000000001000000",
    7: "000000000000000000000000000001100101",
}


def test_parse_input():
    """ Test parse_input function """
    assert day_14.parse_input("./data/day14/test_input.txt") == instructions


def test_decimal_to_binary():
    """ Test decimal_to_binary function """
    assert day_14.decimal_to_binary(11) == "000000000000000000000000000000001011"
    assert day_14.decimal_to_binary(73) == "000000000000000000000000000001001001"
    assert day_14.decimal_to_binary(101) == "000000000000000000000000000001100101"
    assert day_14.decimal_to_binary(0) == "000000000000000000000000000000000000"
    assert day_14.decimal_to_binary(64) == "000000000000000000000000000001000000"


def test_apply_mask():
    """ Test apply_mask function """
    assert (
        day_14.apply_mask("000000000000000000000000000000001011", MASK)
        == "000000000000000000000000000001001001"
    )
    assert (
        day_14.apply_mask("000000000000000000000000000001100101", MASK)
        == "000000000000000000000000000001100101"
    )
    assert (
        day_14.apply_mask("000000000000000000000000000000000000", MASK)
        == "000000000000000000000000000001000000"
    )


def test_apply_char():
    """ Test apply_char function """
    assert (
        day_14.apply_char("000000000000000000000000000000001011", 0, 35)
        == "000000000000000000000000000000001010"
    )
    assert (
        day_14.apply_char("000000000000000000000000000000001011", 1, 33)
        == "000000000000000000000000000000001111"
    )
    assert (
        day_14.apply_char("000000000000000000000000000000001011", "X", 31)
        == "0000000000000000000000000000000X1011"
    )


def test_apply_mask_v2():
    """ Test apply_mask function """
    assert (
        day_14.apply_mask_v2(
            "000000000000000000000000000000101010",
            "000000000000000000000000000000X1001X",
        )
        == "000000000000000000000000000000X1101X"
    )

    assert (
        day_14.apply_mask_v2(
            "000000000000000000000000000000011010",
            "00000000000000000000000000000000X0XX",
        )
        == "00000000000000000000000000000001X0XX"
    )

    # expected = set()


def test_resolve_masked_adress():
    """ Test resolve_masked_address function """
    assert day_14.resolve_masked_address("000000000000000000000000000000X1101X") == [
        "000000000000000000000000000000011010",
        "000000000000000000000000000000011011",
        "000000000000000000000000000000111010",
        "000000000000000000000000000000111011",
    ]

    assert day_14.resolve_masked_address("00000000000000000000000000000001X0XX") == [
        "000000000000000000000000000000010000",
        "000000000000000000000000000000010001",
        "000000000000000000000000000000010010",
        "000000000000000000000000000000010011",
        "000000000000000000000000000000011000",
        "000000000000000000000000000000011001",
        "000000000000000000000000000000011010",
        "000000000000000000000000000000011011",
    ]


def test_sum_mem():
    """ Test sum_mem function """
    assert day_14.sum_mem(mem) == 165


def test_run_instructions():
    """ Test run_instructions function """
    assert day_14.initialize_program.__wrapped__(instructions) == 165


def test_run_instructions_2():
    """ Test run_instructions function """
    assert day_14.initialize_program_v2.__wrapped__(instructions_v2) == 208
