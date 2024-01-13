import app.entities
from app.services import protocols


class ThemeCreate:
    def __init__(
        self,
        uow: protocols.UoW,
        theme_gateway: protocols.ThemeSaver,
    ):
        self._uow = uow
        self._theme_gateway = theme_gateway

    def _to_entity(
        self,
        query_model,
    ) -> app.entities.Theme:
        return app.entities.Theme(
            id=query_model.id,
            name=query_model.name,
        )

    def __call__(self, theme_dto: protocols.ThemeDTO) -> app.entities.Theme:
        theme = app.entities.Theme(
            name=theme_dto.name,
        )
        saved_theme = self._theme_gateway.save(theme)
        self._uow.commit()
        entity = self._to_entity(saved_theme)
        return entity


class ThemeDelete:
    def __init__(
        self,
        uow: protocols.UoW,
        theme_gateway: protocols.ThemeDeleter,
    ):
        self._uow = uow
        self._theme_gateway = theme_gateway

    def __call__(self, theme_id: int):
        self._theme_gateway.delete_by_id(theme_id)
        self._uow.commit()


class ThemeGet:
    def __init__(
        self,
        uow: protocols.UoW,
        theme_gateway: protocols.ThemeReader,
    ):
        self._uow = uow
        self._theme_gateway = theme_gateway

    def __call__(self, theme_id: int) -> app.entities.Theme:
        theme = self._theme_gateway.get_theme_by_id(theme_id)
        self._uow.commit()
        return theme


class ThemeGetList:
    def __init__(
        self,
        uow: protocols.UoW,
        theme_gateway: protocols.ThemeReader,
    ):
        self._uow = uow
        self._theme_gateway = theme_gateway

    def __call__(self) -> list[app.entities.Theme]:
        themes = self._theme_gateway.get_theme_list()
        self._uow.commit()
        return themes
