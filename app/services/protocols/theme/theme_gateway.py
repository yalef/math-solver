import typing
import app.entities


class ThemeSaver(typing.Protocol):
    def save(self, theme: app.entities.Theme):
        pass


class ThemeReader(typing.Protocol):
    def get_theme_by_id(self, theme_id: int) -> app.entities.Theme:
        pass

    def get_theme_list_by_ids(
        self,
        theme_ids: list[int],
    ) -> list[app.entities.Theme]:
        pass

    def get_theme_list(self) -> list[app.entities.Theme]:
        pass


class ThemeDeleter(typing.Protocol):
    def delete_by_id(self, theme_id: int):
        pass
