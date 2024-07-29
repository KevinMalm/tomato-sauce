class UnimplementedFunctionException(Exception):

    file: str
    func: str

    def __init__(self, file: str, func: str) -> None:
        self.file = file
        self.func = func

    def __repr__(self) -> str:
        return f"Unimplemented Exception:: {self.file}::{self.func}(*)"

    def __str__(self) -> str:
        return self.__repr__()
