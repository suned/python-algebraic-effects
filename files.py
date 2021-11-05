from dataclasses import dataclass

from effect import Handler


@dataclass(frozen=True)
class ReadFile:
    name: str


class ReadFileHandler(Handler[ReadFile, str]):
    def handle(self, effect: ReadFile) -> str:
        with open(effect.name) as f:
            return f.read()