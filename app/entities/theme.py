import dataclasses


@dataclasses.dataclass
class Theme:
    name: str
    id: int | None = None

    def __hash__(self):
        return hash(str(self.id))
