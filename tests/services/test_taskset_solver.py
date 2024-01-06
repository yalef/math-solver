import pytest

from app import entities, services
from tests.services import utils


@pytest.fixture
def theme() -> entities.Theme:
    return entities.Theme(
        name="test theme",
    )


@pytest.fixture
def correct_answer() -> entities.Answer:
    return entities.Answer(
        data="correct answer",
        is_correct=True,
    )


@pytest.fixture
def incorrect_answer() -> entities.Answer:
    return entities.Answer(
        data="incorrect answer",
        is_correct=False,
    )


@pytest.fixture
def task(
    theme: entities.Theme,
    correct_answer: entities.Answer,
    incorrect_answer: entities.Answer,
) -> entities.Task:
    return entities.Task(
        answers=[correct_answer, incorrect_answer],
        themes=[theme],
        level=1,
        description="test description",
        img=None,
    )


@pytest.fixture
def taskset(
    task: entities.Task,
) -> entities.TaskSet:
    return entities.TaskSet(
        tasks=[task],
        solved_tasks=[],
        correction_tasks=[],
        failed_tasks=[],
    )


def test_solve_taskset_correct(
    taskset: entities.TaskSet,
    task: entities.Task,
    correct_answer: entities.Answer,
):
    uow = utils.FakeUow()
    taskset_gateway = utils.FakeTaskSetGateway(tasksets=[taskset])
    task_gateway = utils.FakeTaskGateway(tasks=taskset.tasks)

    interactor = services.interactors.TaskSetSolver(
        uow=uow,
        task_gateway=task_gateway,
        taskset_gateway=taskset_gateway,
    )

    result = interactor(
        taskset_id=0,
        task_id=0,
        answer_dto=correct_answer,
    )
    assert task in result.solved_tasks


def test_solve_taskset_incorrect(
    taskset: entities.TaskSet,
    task: entities.Task,
    incorrect_answer: entities.Answer,
):
    uow = utils.FakeUow()
    taskset_gateway = utils.FakeTaskSetGateway(tasksets=[taskset])
    task_gateway = utils.FakeTaskGateway(tasks=taskset.tasks)

    interactor = services.interactors.TaskSetSolver(
        uow=uow,
        task_gateway=task_gateway,
        taskset_gateway=taskset_gateway,
    )

    result = interactor(
        taskset_id=0,
        task_id=0,
        answer_dto=incorrect_answer,
    )
    assert task not in result.solved_tasks
    assert task in result.correction_tasks
