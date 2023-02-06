from PIL import Image


def image_save_to_png(
    size: tuple[int, int],
    map_to_save: list[list[tuple[int, int, int]]],
    map_filename: str = "map_default.png"
):
    image = Image.new("RGB", size, (255, 255, 255))
    pixels = image.load()
    for y in range(size[1]):
        for x in range(size[0]):
            pixels[x, y] = map_to_save[y][x]

    image.save(f"maps/{map_filename}", "PNG")
