import random

from loaders.load_defines import load_terrain_defines


def generate_world(
        size: tuple[int, int]
) -> list[list[tuple[int, int, int]]]:

    (x_size, y_size) = size
    terrain_types = load_terrain_defines()
    terrain_types_by_id = [i for i in range(len(terrain_types))]

    # prepare map
    map_gen: dict[tuple[int, int], list[int]] = dict()
    for x_map in range(x_size):
        for y_map in range(y_size):
            map_gen[(x_map, y_map)] = terrain_types_by_id.copy()

    map_gen = generator(
        map_gen=map_gen
    )

    # convert it to list of rgb colors
    final_map: list[list[tuple[int, int, int]]] = list()
    for x_map in range(x_size):
        final_map.append(list())
        for y_map in range(y_size):
            final_map[x_map].append(terrain_types[map_gen[(x_map, y_map)][0]].rgb)

    return final_map


def generator(
    map_gen: dict[tuple[int, int], list[int]]
) -> dict[tuple[int, int], list[int]]:

    for map_position, map_terrain_id in map_gen.items():
        map_gen[map_position] = [random.choice(map_terrain_id)]

    return map_gen
