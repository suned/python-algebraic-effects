from dataclasses import dataclass

from effect import Handler


class PrintHandler(Handler):
    def handle(self, effect):
        print(effect.msg)

@dataclass(frozen=True)
class Print:
    msg: str
