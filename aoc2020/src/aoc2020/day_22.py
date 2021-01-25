""" Day 22: Crab Combat """
import os
from copy import copy
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input"""
    deck_1 = []
    deck_2 = []
    current = deck_1
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            if line.startswith("Player"):
                continue

            if line == "\n":
                current = deck_2
                continue

            current.append(int(line.strip()))

    return deck_1, deck_2


def play(deck_1, deck_2):
    """ Play a game of combat """
    player_1 = copy(deck_1)
    player_2 = copy(deck_2)

    while len(player_1) > 0 and len(player_2) > 0:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if card_1 > card_2:
            player_1 += [card_1, card_2]
        else:
            player_2 += [card_2, card_1]

    return player_1 if len(player_1) > 0 else player_2


def play_recursive(deck_1, deck_2):
    """ Play a game of recursive combat """
    played_decks = set()
    player_1 = copy(deck_1)
    player_2 = copy(deck_2)

    if player_1 == [8] and player_2 == [10, 9, 7, 5]:
        click.echo("Found")

    while len(player_1) > 0 and len(player_2) > 0:
        winner_1 = False
        if (tuple(player_1), tuple(player_2)) in played_decks:
            card_1 = player_1.pop(0)
            card_2 = player_2.pop(0)

            player_1 += [card_1, card_2]
            return (True, deck_1)

        played_decks.add((tuple(player_1), tuple(player_2)))

        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if len(player_1) >= card_1 and len(player_2) >= card_2:
            (winner_1, _) = play_recursive(player_1[:card_1], player_2[:card_2])

        else:
            winner_1 = card_1 > card_2

        if winner_1:
            player_1 += [card_1, card_2]
        else:
            player_2 += [card_2, card_1]

    return (True, player_1) if len(player_1) > 0 else (False, player_2)


def calculate_score(deck):
    """Calculate the score of the deck"""
    acc = 0
    for (index, card) in enumerate(reversed(deck)):
        acc += (index + 1) * card

    return acc


@timer
def part_1(deck_1, deck_2):
    """ Solve part 1"""
    deck = play(deck_1, deck_2)
    return calculate_score(deck)


@timer
def part_2(deck_1, deck_2):
    """ Solve part 1"""
    (_, deck) = play_recursive(deck_1, deck_2)
    return calculate_score(deck)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 22 Main """
    deck_1, deck_2 = parse_input(input_path)

    click.echo("Day 22: Crab Combat")
    click.echo(f"Part 1: {part_1(deck_1, deck_2)}")
    click.echo(f"Part 2: {part_2(deck_1, deck_2)}")
