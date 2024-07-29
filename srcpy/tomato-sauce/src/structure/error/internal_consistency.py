class InternalConsistencyCheckException(Exception):

    file: str
    error: str

    def __init__(self, file: str, error: str) -> None:
        self.file = file
        self.error = error

    def __repr__(self) -> str:
        return f"Internal Consistency Check Failed. {self.error}. In {self.file}"

    def __str__(self) -> str:
        return self.__repr__()
