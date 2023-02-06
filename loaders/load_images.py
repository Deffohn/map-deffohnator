from PIL import Image
import yaml

from classes.terrains import TerrainType


def get_wfc_defines(
    yaml_file: str = "defines/wfc_defines.yaml"
) -> list[tuple[int, int]]:
    data: dict
    with open(yaml_file, "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    if "prox_coordinates" not in data.keys():
        raise KeyError(f"Error in wfc_defines: \"prox_coordinates\" field does not exists.")

    prox_defines: list[tuple[int, int]] = list()
    for index, prox_coors in enumerate(data["prox_coordinates"]):
        if "x" not in prox_coors.keys():
            raise KeyError(f"Error in {index}th element "
                           f"in terrain_defines: x field does "
                           f"not exists.")
        x = prox_coors["x"]
        if "y" not in prox_coors.keys():
            raise KeyError(f"Error in {index}th element "
                           f"in terrain_defines: y field does "
                           f"not exists.")
        y = prox_coors["y"]
        prox_defines.append((x, y))

    return prox_defines


# patterns for wave function collapse
def get_map_patterns_from_image_for_wfc(
    terrain_types: list[TerrainType],
    image: str = "pattern_default.png",
) -> dict[int, dict[tuple[int, int], int]]:  # { id : { prox_coordinates : id, }, }
    """

    :param terrain_types:
    :param image:
    :return: map of ids joined to ids by proximity
    """

    # Open the image
    img = Image.open(f"images/{image}")

    # Get the pixels
    open_pixels = list(img.getdata())
    width, height = img.size
    rgb_pixels: list[list[tuple[int, int, int]]] = [open_pixels[i * width: (i + 1) * width] for i in range(height)]

    # Convert pixels to their ids
    pixels_by_id: list[list[int]] = list()
    for i, rgb_pixels_row in enumerate(rgb_pixels):
        pixels_by_id.append(list())
        for j, rgb_pixel in enumerate(rgb_pixels_row):

            for terrain_type in terrain_types:
                if terrain_type.rgb == rgb_pixel:
                    pixels_by_id[i].append(terrain_type.type_id)
                    break

            if len(pixels_by_id[i]) <= j:
                raise(ValueError(f"Pixel at ({i}, {j}) is matching no terrain type."))

    map_patterns: dict[int, dict[tuple[int, int], list[int]]] = dict()
    for terrain_type in range(len(terrain_types)):
        map_patterns[terrain_type]: dict[tuple[int, int], int] = dict()

    prox_coors = get_wfc_defines()
    for y_map in range(height):
        for x_map in range(width):
            terrain_id = pixels_by_id[x_map][y_map]
            if terrain_id not in map_patterns.keys():
                map_patterns[terrain_id] = dict()

            for prox_coordinate in prox_coors:
                if 0 <= x_map + prox_coordinate[0] < width and 0 <= y_map + prox_coordinate[1] < height :

                    if prox_coordinate not in map_patterns[terrain_id].keys():
                        map_patterns[terrain_id][prox_coordinate] = list()

                    if pixels_by_id[x_map + prox_coordinate[0]][y_map + prox_coordinate[1]] \
                            not in map_patterns[terrain_id][prox_coordinate]:
                        map_patterns[terrain_id][prox_coordinate].append(
                            pixels_by_id[x_map + prox_coordinate[0]][y_map + prox_coordinate[1]]
                        )



    return map_patterns
