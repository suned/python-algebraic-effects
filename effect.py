class Handler:
    def handle(self, effect):
        raise NotImplementedError()


def run(c, handlers):
    try:
        effect = next(c)
        while True:
            result = handlers[type(effect)].handle(effect)
            effect = c.send(result)
    except StopIteration as stop:
        return stop.value