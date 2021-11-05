from dataclasses import dataclass

from effect import Handler


@dataclass(frozen=True)
class Print:
    msg: str


class PrintHandler(Handler[Print, None]):
    def handle(self, effect: Print) -> None:
        print(effect.msg)
