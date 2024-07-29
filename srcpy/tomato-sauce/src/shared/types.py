from dataclasses import dataclass
from uuid import uuid4


@dataclass()
class String:
    string: str

    @staticmethod
    def empty():
        return String("")

    def __str__(self) -> str:
        return self.string

    def __hash__(self) -> int:
        return self.string.__hash__()

    def sanitize(self):
        self.string = self.string.replace('"', "`").replace("'", "`")
        return self.string


@dataclass
class Number:
    number: float

    def __str__(self) -> str:
        return str(self.number)

    def __hash__(self) -> int:
        return self.number.__hash__()


def uuid() -> String:
    return String(str(uuid4()))
