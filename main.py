from loaders.load_defines import load_terrain_defines
from tools import dir_tools


if __name__ == '__main__':
    print("maps folder ready :", dir_tools.scan_create_directory_location("maps"))
    print(load_terrain_defines())
