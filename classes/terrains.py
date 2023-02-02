

class TerrainType:
    id: int
    name: str
    rgb: tuple[int, int, int]

    def __init__(
            self,
            type_id: int,
            name: str,
            rgb: tuple[int, int, int]
    ):
        self.id = type_id
        self.name = name
        self.rgb = rgb

    def __repr__(self):
        return f"(id:{self.id}, name: {self.name}, rgb: {self.rgb})"

    def __reduce__(self):
        return TerrainType, (self.id, self.name, self.rgb)


class TerrainPixel:
    terrain_type_id: int
    coordinates: tuple[int, int]

    def __init__(
            self,
            terrain_type_id: int,
            coordinates: tuple[int, int]
    ):
        self.terrain_type_id = terrain_type_id
        self. coordinates = coordinates

