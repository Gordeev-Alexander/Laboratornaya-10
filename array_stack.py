from typing import Any
from .base import IStack

class ArrayStack(IStack[Any]):

    def __init__(self):
        self._data = []

    def empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> None:
        if self.empty():
            raise IndexError("pop from empty stack")
        self._data.pop()

    def top(self) -> Any:
        if self.empty():
            raise IndexError("top from empty stack")
        return self._data[-1]