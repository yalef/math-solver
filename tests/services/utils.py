from app.services import protocols
from app import entities


class FakeUow(protocols.UoW):
    def commit(self):
        pass

    def rollback(self):
        pass


class FakeTaskGateway(protocols.TaskReader):
    def __init__(self, tasks: list[entities.Task]):
        self._tasks = tasks

    def get_task_by_id(self, task_id: int) -> entities.Task:
        if task_id > len(self._tasks) - 1:
            raise Exception("There're no tasks with such id.")
        return self._tasks[task_id]

    def get_tasks_by_ids(self, task_ids: int):
        return ...

    def get_tasks_list(self):
        ...

    def get_tasks_list_by_taskset_id(self, taskset_id: int):
        ...


class FakeTaskSetGateway(protocols.TaskSetSaver, protocols.TaskSetReader):
    def __init__(self, tasksets: list[entities.TaskSet]):
        self._tasksets = tasksets

    def get_taskset_by_id(self, id: int) -> entities.TaskSet:
        if id > len(self._tasksets) - 1:
            raise Exception("There're no taskset with such id.")
        return self._tasksets[id]

    def get_taskset_list(self):
        ...

    def save(self, taskset: entities.TaskSet):
        ...
