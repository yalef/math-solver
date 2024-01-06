import dataclasses


@dataclasses.dataclass
class Theme:
    name: str
    id: int | None = None
