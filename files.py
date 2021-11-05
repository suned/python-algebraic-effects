from dataclasses import dataclass

from effect import Handler


@dataclass(frozen=True)
class ReadFile:
    name: str

class ReadFileHandler(Handler):
    def handle(self, effect):
        with open(effect.name) as f:
            return f.read()