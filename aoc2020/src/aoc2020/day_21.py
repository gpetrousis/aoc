""" Day 21: Allergen Assessment """
import os
import re
from copy import deepcopy
from collections import defaultdict
import click
from aoc2020.timer import timer


def parse_input(input_path):
    """Parse the input into a dict of alergen: set(ingredients)
    and ingredients[count]"""
    allergen_ingredients = dict()

    with open(os.path.abspath(input_path)) as input_file:
        lines = list(input_file)
        all_ingredients = defaultdict(int)

        pattern = re.compile(r"^(.*) \(contains (.*)\)$")

        for line in lines:
            match = re.match(pattern, line)
            ingredients = match.group(1).split(" ")
            allergens = match.group(2).split(", ")

            for allergen in allergens:
                if allergen in allergen_ingredients:
                    allergen_ingredients[allergen].intersection_update(set(ingredients))
                else:
                    allergen_ingredients[allergen] = set(ingredients)

            for ingredient in ingredients:
                all_ingredients[ingredient] += 1

    return allergen_ingredients, all_ingredients


def find_non_allergens(allergens, ingredients_count):
    """ Find the ingredients that are not alergens """
    non_allergens = set(ingredients_count.keys())
    for ingredients in allergens.values():
        for ingredient in ingredients:
            non_allergens.discard(ingredient)

    return non_allergens


def resolve_allergens(allergens):
    """ Resolve the alergens to ingredients """
    resolved_allergens = deepcopy(allergens)
    resolved_ingredients = set()

    done = False
    while not done:
        done = True
        for ingredients in resolved_allergens.values():
            if len(ingredients) == 1:
                resolved_ingredients.update(ingredients)
            else:
                ingredients -= resolved_ingredients
                done = False

    return resolved_allergens


@timer
def count_non_alergens(allergens, ingredients):
    """ Count the how many times the ingredients that have no alergens """
    non_allergens = find_non_allergens(allergens, ingredients)
    return sum([ingredients[x] for x in non_allergens])


@timer
def generate_dangerous_ingredient(allergens):
    """ Generate the dangerous ingredient list """
    resolved_allergens = resolve_allergens(allergens)

    ingredient_list = []
    sorted_allergens = sorted(resolved_allergens.keys())
    for allergen in sorted_allergens:
        ingredient_list.append(*resolved_allergens[allergen])

    return ",".join(ingredient_list)


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 21 Main """
    allergens, ingredients = parse_input(input_path)

    click.echo("Day 21: Allergen Assessment")
    click.echo(f"Part 1: {count_non_alergens(allergens, ingredients)}")
    click.echo(f"Part 2: {generate_dangerous_ingredient(allergens)}")
