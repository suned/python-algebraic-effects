# python-algebraic-effects
Purely Functional, Coroutine based algebraic effects in Python

# Example:
```python
from ask import Ask, AskHandler
from files import ReadFile, ReadFileHandler
from console import Print, PrintHandler
from effect import run


def f():
    name = yield Ask()
    content = yield ReadFile(name)
    return content


def test():
    content = yield from f()
    yield Print(content)
    return 'done'


handlers = {ReadFile : ReadFileHandler(),
            Ask      : AskHandler('effect.py'),
            Print    : PrintHandler()}
run(test(), handlers)
```
