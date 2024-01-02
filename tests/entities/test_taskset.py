import pytest
from app.entities import TaskSet, Task, Answer, Theme


@pytest.fixture
def theme() -> Theme:
    return Theme("matrix")


@pytest.fixture
def correct_answer() -> Answer:
    return Answer("some data", is_correct=True)


@pytest.fixture
def incorrect_answer() -> Answer:
    return Answer("some data", is_correct=False)


def test_solve_taskset_correct(
    theme: Theme,
    correct_answer: Answer,
):
    task = Task(
        answers=[correct_answer],
        themes=[theme],
        level=1,
        description="test description",
        img=None,
    )
    taskset = TaskSet(
        [task],
        [],
        [],
        [],
    )
    taskset.solve_task(task, correct_answer)
    assert task in taskset.solved_tasks
    assert taskset.is_solved


def test_solve_taskset_incorrect(
    theme: Theme,
    incorrect_answer: Answer,
):
    task = Task(
        answers=[incorrect_answer],
        themes=[theme],
        level=1,
        description="test description",
        img=None,
    )
    taskset = TaskSet(
        [task],
        [],
        [],
        [],
    )
    taskset.solve_task(task, incorrect_answer)
    assert task in taskset.correction_tasks
    assert not taskset.is_solved

    taskset.solve_task(task, incorrect_answer)
    assert task in taskset.failed_tasks
    assert taskset.is_solved
