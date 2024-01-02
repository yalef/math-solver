import typing


class ThemeDTO(typing.Protocol):
    id: int | None
    name: str
