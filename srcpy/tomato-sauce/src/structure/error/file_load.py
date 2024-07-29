class FileLoadError(Exception):

    file: str
    target_struct: str
    message: str

    def __init__(self, file: str, target: str, message: str) -> None:
        self.file = file
        self.target_struct = target
        self.message = message
        super().__init__()

    def __repr__(self) -> str:
        return f"File Load Error: Failed to process {self.target_struct} at `{self.file}` due to {self.message}"

    def __str__(self) -> str:
        return self.__repr__()
