from image_parser import image_save_to_png
from loaders.load_defines import load_terrain_defines
from loaders.load_images import get_map_patterns_from_image_for_wfc
from tools import dir_tools
from wfc_generator import generate_world

if __name__ == '__main__':
    print("maps folder ready :", dir_tools.scan_create_directory_location("maps"))

    terrain_types = load_terrain_defines()
    print("Terrain types:", terrain_types)

    map_size = (15, 15)

    map_generated = generate_world(
        size=map_size,
    )

    image_save_to_png(
        size=map_size,
        map_to_save=map_generated,
        map_filename="test_full_random.png",
    )


