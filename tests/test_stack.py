import pytest
from stack.array_stack import ArrayStack

def test_empty_and_size():
    stack = ArrayStack()
    assert stack.empty()
    assert stack.size() == 0

    stack.push(42)
    assert not stack.empty()
    assert stack.size() == 1

def test_push_pop_top():
    stack = ArrayStack()
    stack.push("hello")
    stack.push("world")

    assert stack.top() == "world"
    stack.pop()
    assert stack.top() == "hello"
    stack.pop()
    assert stack.empty()

def test_pop_empty():
    stack = ArrayStack()
    with pytest.raises(IndexError, match="pop from empty stack"):
        stack.pop()

def test_top_empty():
    stack = ArrayStack()
    with pytest.raises(IndexError, match="top from empty stack"):
        stack.top()

def test_with_different_types():
    int_stack = ArrayStack()
    int_stack.push(1)
    int_stack.push(2)
    assert int_stack.top() == 2

    str_stack = ArrayStack()
    str_stack.push("a")
    str_stack.push("b")
    assert str_stack.top() == "b"

    float_stack = ArrayStack()
    float_stack.push(3.14)
    assert float_stack.top() == 3.14