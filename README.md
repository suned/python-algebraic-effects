# python-algebraic-effects
Purely Functional, coroutine based algebraic effects in Python

# Example:
```python
from typing import Generator, Union, Any, Dict, Type

from ask import Ask, AskHandler
from files import ReadFile, ReadFileHandler
from console import Print, PrintHandler
from effect import run, Handler


def f() -> Generator[Union[Ask, ReadFile], Any, str]:
    name: str = yield Ask()
    content: str = yield ReadFile(name)
    return content


def test() -> Generator[Union[Ask, ReadFile, Print], Any, str]:
    content: str = yield from f()
    yield Print(content)
    return 'done'


handlers: Dict[Type, Handler] = {
    ReadFile : ReadFileHandler(),
    Ask      : AskHandler('effect.py'),
    Print    : PrintHandler()
}
run(test(), handlers)
```
