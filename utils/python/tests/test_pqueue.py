from ..pqueue import PriorityQueue
import pytest

def test_pq_len():
    pq = PriorityQueue()
    assert len(pq) == 0
    pq.push(priority=2, item="b")
    pq.push(priority=3, item="a")
    pq.push(priority=1, item="c")
    assert len(pq) == 3
    pq.pop()
    assert len(pq) == 2

def test_pq_top():
    pq = PriorityQueue()
    pq.push(priority=2, item="b")
    pq.push(priority=3, item="a")
    pq.push(priority=1, item="c")
    pq_item = pq.top()
    assert pq_item.priority == 1 and pq_item.item == "c"
    pq.pop()
    pq_item = pq.top()
    assert pq_item.priority == 2 and pq_item.item == "b"
    pq.pop()
    pq_item = pq.top()
    assert pq_item.priority == 3 and pq_item.item == "a"
    pq.pop()
    with pytest.raises(IndexError):
        pq.top()

def test_min_pq():
    pq = PriorityQueue()
    pq.push(priority=2, item="b")
    pq.push(priority=3, item="a")
    pq.push(priority=2, item="bb")
    pq.push(priority=1, item="c")
    pq_item = pq.pop()
    assert pq_item.priority == 1 and pq_item.item == "c"
    pq_item = pq.pop()
    assert pq_item.priority == 2 and pq_item.item == "b"
    pq_item = pq.pop()
    assert pq_item.priority == 2 and pq_item.item == "bb"
    pq_item = pq.pop()
    assert pq_item.priority == 3 and pq_item.item == "a"
    with pytest.raises(IndexError):
        pq.pop()

def test_max_pq():
    pq = PriorityQueue(max_queue=True)
    pq.push(priority=2, item="b")
    pq.push(priority=3, item="a")
    pq.push(priority=2, item="bb")
    pq.push(priority=1, item="c")
    pq_item = pq.pop()
    assert pq_item.priority == 3 and pq_item.item == "a"
    pq_item = pq.pop()
    assert pq_item.priority == 2 and pq_item.item == "b"
    pq_item = pq.pop()
    assert pq_item.priority == 2 and pq_item.item == "bb"
    pq_item = pq.pop()
    assert pq_item.priority == 1 and pq_item.item == "c"
    with pytest.raises(IndexError):
        pq.pop()
