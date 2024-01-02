import typing
import app.entities


class TaskSetSaver(typing.Protocol):
    def save(self, taskset: app.entities.TaskSet):
        pass


class TaskSetReader(typing.Protocol):
    def get_taskset_list(self) -> list[app.entities.TaskSet]:
        pass

    def get_taskset_by_id(self, id: int) -> app.entities.TaskSet:
        pass
