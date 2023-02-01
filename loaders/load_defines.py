from classes.terrains import TerrainType
import yaml


def load_terrain_defines(
        yaml_file: str = "defines/terrain_defines.yaml"
) -> list[TerrainType]:

    data: dict
    with open(yaml_file, "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    terrain_types: list[TerrainType] = list()
    for index, terrain_type in enumerate(data):
        if "id" not in terrain_type.keys():
            raise KeyError(f"Error in {index}th element "
                           f"in terrain_defines: id field does "
                           f"not exists")
        type_id = terrain_type["id"]
        if "name" not in terrain_type.keys():
            raise KeyError(f"Error in {index}th element "
                           f"in terrain_defines: name field does "
                           f"not exists")
        name = terrain_type["name"]
        if "rgb" not in terrain_type.keys():
            raise KeyError(f"Error in {index}th element "
                           f"in terrain_defines: rgb field does "
                           f"not exists")
        rgb = terrain_type["rgb"]
        terrain_types.append(TerrainType(
            id=type_id,
            name=name,
            rgb=rgb
        ))

    return terrain_types
