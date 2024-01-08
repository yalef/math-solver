import typing

import app.entities


class TaskSaver(typing.Protocol):
    def save(self, task: app.entities.Task):
        pass

    def save_batch(self, tasks: list[app.entities.Task]):
        pass


class TaskReader(typing.Protocol):
    def get_tasks_list(self) -> list[app.entities.Task]:
        pass

    def get_tasks_list_by_taskset_id(
        self,
        taskset_id: int,
    ) -> list[app.entities.Task]:
        pass

    def get_task_by_id(self, task_id: int) -> app.entities.Task:
        pass

    def get_tasks_by_ids(self, task_ids: list[int]) -> list[app.entities.Task]:
        pass

    def get_task_without_taskset_by_theme_and_level(
        self,
        theme: app.entities.Theme,
        level: int,
    ) -> app.entities.Task:
        pass


class TaskDeleter(typing.Protocol):
    def delete_by_id(self, task_id: int):
        pass
