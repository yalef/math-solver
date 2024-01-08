import sqlalchemy as sa
from app import entities
from app.adapters.database import gateways, models, utils

engine = utils.build_engine(
    db_url="postgresql://postgres:postgres@localhost:5432/postgres",
)
session_factory = utils.build_session_factory(engine)


with session_factory() as session:
    theme_query = sa.select(models.ThemeDBModel)
    theme_instance = session.scalars(theme_query).unique()
    theme_ids = []
    for theme in theme_instance:
        theme_ids.append(theme.id)

    query = sa.select(models.TaskDBModel).where(
        models.TaskDBModel.themes.any(models.ThemeDBModel.id.in_(theme_ids)),
    )
    instances = session.scalars(query).unique()
    session.commit()
    breakpoint()
