from typing import Generator, TypeVar, Generic, Type, Dict, Any


E = TypeVar('E')
R = TypeVar('R')


class Handler(Generic[E, R]):
    def handle(self, effect: E) -> R:
        raise NotImplementedError()


A = TypeVar('A')

def run(c: Generator[Any, Any, A], handlers: Dict[Type, Handler]) -> A:
    try:
        effect = next(c)
        while True:
            result = handlers[type(effect)].handle(effect)
            effect = c.send(result)
    except StopIteration as stop:
        return stop.value