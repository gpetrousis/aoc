""" Day 20: Jurassic Jigsaw """
import os
import re
from math import prod, sqrt
from copy import deepcopy
import click
from aoc2020.timer import timer

MONSTER = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]


class Tile:
    """ Class to represent a tile of the image """
    def __init__(self, tile_id, grid):
        self.id = tile_id
        self.grid = grid
        self.neighbours = set()

    def rotate(self):
        """ Rotate 90 degrees clockwise """
        self.grid = list(zip(*self.grid[::-1]))

    def flip(self):
        """ Flip the tile horizontaly """
        self.grid = list(reversed(self.grid))

    def get_top_border(self):
        """ Get the top border of the tile """
        return self.grid[0]

    def get_bottom_border(self):
        """ Get the bottom border of the tile """
        return self.grid[-1]

    def get_left_border(self):
        """ Get the left border of the tile """
        return tuple([row[0] for row in self.grid])

    def get_right_border(self):
        """ Get the right border of the tile """
        return tuple([row[-1] for row in self.grid])

    def get_all_borders(self):
        """ Get all the borders """
        return [
            self.get_top_border(),
            self.get_bottom_border(),
            self.get_left_border(),
            self.get_right_border(),
        ]

    def add_neighbour(self, neighbour_id):
        """ Add another tile id to the neighbour list """
        self.neighbours.add(neighbour_id)

    def get_sides(self):
        """ Add get all the sides of the Tile including the reversed """
        sides = set()

        borders = self.get_all_borders()
        sides.update(borders)
        sides.update(map(lambda x: tuple(reversed(x)), borders))

        return sides

    def get_pixels(self):
        """ Get the tile without its borders """
        pixels = []
        for row in self.grid[1:-1]:
            pixels.append(row[1:-1])

        return pixels


def parse_input(input_path):
    """Parse the input"""
    tiles = []
    id_pattern = re.compile(r"^Tile (\d*):$")
    with open(os.path.abspath(input_path)) as input_file:
        lines = list(input_file)
        grid = []
        for line in lines:
            match = re.match(id_pattern, line)
            if match:
                tile_id = int(match.group(1))
            elif line == "\n":
                tiles.append(Tile(tile_id=tile_id, grid=grid))
                grid = []
            else:
                grid.append(tuple(line.strip()))

        tiles.append(Tile(tile_id=tile_id, grid=grid))

    return tiles


def get_monster_offsets():
    """ Return the offsets based on the monster image """
    offsets = []
    for (row, line) in enumerate(MONSTER):
        for (column, letter) in enumerate(line):
            if letter == "#":
                offsets.append((column, row))

    return offsets


def count_monsters(image):
    """ Count the number of monsters in the image """
    monster_offsets = get_monster_offsets()
    count = 0
    for row in range(0, len(image) - 3):
        for column in range(0, len(image[row]) - 20):
            found = True
            for (step_x, step_y) in monster_offsets:
                if image[row + step_y][column + step_x] != "#":
                    found = False
                    break
            if found:
                count += 1

    return count


def get_neighbours(tiles):
    """ Calculate the neighbours of each tile """
    checked = []

    for tile_x in tiles:
        sides_x = tile_x.get_sides()
        for tile_y in tiles:
            if tile_x.id == tile_y.id:
                continue

            if tile_y.id in checked:
                continue

            sides_y = tile_y.get_sides()
            common = sides_x & sides_y

            if len(common) > 0:
                tile_x.add_neighbour(tile_y)
                tile_y.add_neighbour(tile_x)

        checked.append(tile_x.id)


def construct_image(sorted_tiles):
    """ Construct the image based on the sorted tiles """
    row = 0
    image = []
    for image_row in sorted_tiles:
        for _ in range(8):
            image.append([])

        for tile in image_row:
            for (index, pixel_row) in enumerate(tile.get_pixels()):
                image[row + index] += pixel_row

        row += 8

    return image


def find_adjustent_tile_right(current, placed):
    """ Find the neighbour tile that is adjastent to the right side """
    for tile in current.neighbours:
        if tile.id in placed or current.get_right_border() not in tile.get_sides():
            continue

        rotations = 0
        while current.get_right_border() != tile.get_left_border():
            if rotations < 3:
                tile.rotate()
                rotations += 1
            else:
                tile.flip()
                rotations = 0

        return tile


def find_adjustent_tile_bottom(current, placed):
    """ Find the neighbour tile that is adjastent to the bottom side """
    for tile in current.neighbours:
        if tile.id in placed or current.get_bottom_border() not in tile.get_sides():
            continue

        rotations = 0
        while current.get_bottom_border() != tile.get_top_border():
            if rotations < 3:
                tile.rotate()
                rotations += 1
            else:
                tile.flip()
                rotations = 0

        return tile


def sort_tiles(tiles, corner_tiles):
    """ Sort the tiles based on the neighbour borders """
    sorted_tiles = [[]]
    placed = []

    # Starting from a corner tile
    current = next(tile for tile in tiles if tile.id in corner_tiles)

    # Find the corner orientation and the neighbohrs orientation
    # so that the two neighbohrs fit the right and bottom sides
    neighbour_1, neighbour_2 = current.neighbours

    neighbour_borders_1 = neighbour_1.get_sides()
    neighbour_borders_2 = neighbour_2.get_sides()

    rotations = 0
    while not (
        current.get_right_border() in neighbour_borders_1
        and current.get_bottom_border() in neighbour_borders_2
    ) or (
        current.get_bottom_border() in neighbour_borders_1
        and current.get_right_border() in neighbour_borders_2
    ):
        if rotations < 3:
            current.rotate()
            rotations += 1
        else:
            current.flip()
            rotations = 0

    sorted_tiles[0].append(current)
    placed.append(current.id)

    image_size = int(sqrt(len(tiles)))

    # Add the rest of the line
    for _ in range(image_size - 1):
        next_tile = find_adjustent_tile_right(current, placed)
        sorted_tiles[0].append(next_tile)
        placed.append(next_tile)
        current = next_tile

    current = sorted_tiles[0][0]

    # Add the rest of the lines
    for index in range(1, image_size):
        # Add the first tile of the next line
        sorted_tiles.append([find_adjustent_tile_bottom(current, placed)])
        current = sorted_tiles[index][0]
        for _ in range(image_size - 1):
            next_tile = find_adjustent_tile_right(current, placed)
            sorted_tiles[index].append(next_tile)
            placed.append(next_tile)
            current = next_tile

        current = sorted_tiles[index][0]

    return sorted_tiles


def get_corner_tiles(tiles):
    """ Get the corner tiles """
    return [tile.id for tile in tiles if len(tile.neighbours) == 2]


@timer
def mult_corner_tiles(tiles):
    """ Return the product of the corner tiles """
    # Copying the tiles so the timing will be more accurate
    _tiles = deepcopy(tiles)
    get_neighbours(_tiles)
    corner_tiles = get_corner_tiles(_tiles)
    return prod(corner_tiles)


@timer
def search_for_monsters(tiles):
    """ Return the pixels that are not part of monsters """
    # Copying the tiles so the timing will be more accurate
    _tiles = deepcopy(tiles)
    get_neighbours(_tiles)
    corner_tiles = get_corner_tiles(_tiles)
    sorted_tiles = sort_tiles(_tiles, corner_tiles)
    image = construct_image(sorted_tiles)
    image_tile = Tile("Image", image)

    rotations = 0

    monsters = count_monsters(image_tile.grid)
    while monsters == 0:
        if rotations < 4:
            image_tile.rotate()
            rotations += 1
        else:
            image_tile.flip()
            rotations = 0
        monsters = count_monsters(image_tile.grid)

    monster_pixels = monsters * 15
    all_pixels = sum(map(lambda x: x.count("#"), image))

    return all_pixels - monster_pixels


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 20 Main """
    tiles = parse_input(input_path)

    click.echo("Day 20: Jurassic Jigsaw")
    click.echo(f"Part 1: {mult_corner_tiles(tiles)}")
    click.echo(f"Part 1: {search_for_monsters(tiles)}")
