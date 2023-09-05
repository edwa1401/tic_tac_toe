class AppError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg


class ParseError(AppError):
    def __init__(self, msg: str, cmd: str) -> None:
        super().__init__(msg)
        self.cmd = cmd
