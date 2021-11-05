from dataclasses import dataclass

from effect import Handler


@dataclass(frozen=True)
class Ask:
    pass


class AskHandler(Handler):
    def __init__(self, value):
        self.value = value

    def handle(self, _):
        return self.value