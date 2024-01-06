from app import entities
from app.adapters.database import gateways, models, utils

engine = utils.build_engine(
    db_url="postgresql://postgres:postgres@localhost:5432/postgres",
)
session_factory = utils.build_session_factory(engine)


with session_factory() as session:
    taskset = entities.TaskSet(id=None, name="New Taskset", tasks=[])
    taskset_gateway = gateways.TaskSetDBGateway(session)
    taskset_gateway.save(taskset)
    tasksets = taskset_gateway.get_taskset_list()
    print(tasksets)

    theme = entities.Theme(
        id=None,
        name="New theme",
    )
    theme_gateway = gateways.ThemeDBGateway(session)
    theme_gateway.save(theme)
    themes = theme_gateway.get_theme_list()
    print(themes)

    task = entities.Task(
        id=None,
        taskset_id=tasksets[0].id,
        answers=[],
        themes=[themes[0]],
        level=1,
        description="test desc",
        status=entities.TaskStatus.started,
    )
    task_gateway = gateways.TaskDBGateway(session)
    task_gateway.save(task)
    tasks = task_gateway.get_task_list()
    print(tasks)

    session.commit()
