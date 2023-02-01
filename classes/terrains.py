

class TerrainType:
    id: int
    name: str
    rgb: tuple[int, int, int]

    def __init__(
            self,
            id: int,
            name: str,
            rgb: tuple[int, int, int]
    ):
        self.id = id
        self.name = name
        self. rgb = rgb

    def __reduce__(self):
        return TerrainType, (self.id, self.name, self.rgb)

