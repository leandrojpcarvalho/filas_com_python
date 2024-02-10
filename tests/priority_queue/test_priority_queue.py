from ting_file_management.priority_queue import PriorityQueue
import pytest

data = [
    {
        "qtd_linhas": 5,
    },
    {
        "qtd_linhas": 10,
    },
    {
        "qtd_linhas": 15,
    },
    {
        "qtd_linhas": 4,
    },
    {
        "qtd_linhas": 2,
    },
    {
        "qtd_linhas": 1,
    },
]


def test_basic_priority_queueing():
    instance = PriorityQueue()

    for indigent_element in data:
        instance.enqueue(indigent_element)

    assert instance.dequeue() == {"qtd_linhas": 4}
    assert instance.dequeue() == {"qtd_linhas": 2}

    assert instance.search(0) == {"qtd_linhas": 1}
    assert instance.search(1) == {"qtd_linhas": 5}

    with pytest.raises(IndexError):
        instance.search("a")
