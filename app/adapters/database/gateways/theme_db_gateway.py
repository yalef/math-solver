import sqlalchemy as sa
from sqlalchemy import orm

from app import entities
from app.adapters.database import models
from app.services import protocols


class ThemeDBGateway(
    protocols.ThemeReader,
    protocols.ThemeSaver,
    protocols.ThemeDeleter,
):
    model = models.ThemeDBModel

    def __init__(self, session: orm.Session):
        self._session = session

    def _to_entity(
        self,
        query_model: models.ThemeDBModel,
    ) -> entities.Theme:
        return entities.Theme(
            id=query_model.id,
            name=query_model.name,
        )

    def save(self, theme: entities.Theme) -> entities.Theme:
        if theme.id is None:
            instance = self.model(
                name=theme.name,
            )
            self._session.add(instance)
            return self._to_entity(instance)
        else:
            query = sa.select(self.model).where(self.model.id == theme.id)
            instance = self._session.scalars(query).one()
            instance.name = theme.name
            return self._to_entity(instance)

    def get_theme_by_id(self, theme_id: int) -> entities.Theme:
        query = sa.select(self.model).where(self.model.id == theme_id)
        instance = self._session.scalars(query).unique().one()
        return self._to_entity(instance)

    def get_theme_list_by_ids(
        self,
        theme_ids: list[int],
    ) -> list[entities.Theme]:
        query = sa.select(self.model).where(self.model.id.in_(theme_ids))
        instances = self._session.scalars(query).unique()
        return [self._to_entity(instance) for instance in instances]

    def get_theme_list(self) -> list[entities.Theme]:
        query = sa.select(self.model)
        instances = self._session.scalars(query).unique().all()
        return [self._to_entity(instance) for instance in instances]

    def delete_by_id(self, theme_id: int):
        query = sa.select(self.model).where(self.model.id == theme_id)
        instance = self._session.scalars(query).unique().one()
        self._session.delete(instance)
