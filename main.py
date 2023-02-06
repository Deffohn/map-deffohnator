from loaders.load_defines import load_terrain_defines
from loaders.load_images import get_map_patterns_from_image_for_wfc
from tools import dir_tools


if __name__ == '__main__':
    print("maps folder ready :", dir_tools.scan_create_directory_location("maps"))

    terrain_types = load_terrain_defines()
    print("Terrain types:", terrain_types)

    print(get_map_patterns_from_image_for_wfc(
        terrain_types=terrain_types,
    ))
