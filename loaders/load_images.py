from PIL import Image

from classes.terrains import TerrainType


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

    map_patterns: dict[int, dict[tuple[int, int], int]] = dict()

    # TODO finish feature getting ids pattern associations

    return map_patterns
