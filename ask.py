from typing import TypeVar
from dataclasses import dataclass

from effect import Handler


@dataclass(frozen=True)
class Ask:
    pass


A = TypeVar('A')


class AskHandler(Handler[Ask, A]):
    def __init__(self, value: A):
        self.value = value

    def handle(self, _: Ask) -> A:
        return self.value