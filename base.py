from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class IStack(ABC, Generic[T]):

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> None:
        pass

    @abstractmethod
    def top(self) -> T:
        pass