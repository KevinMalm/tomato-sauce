from dataclasses import dataclass
from shared.types import String
from typing import List


@dataclass
class BookResponse:
    title: String
    author: String
    summary: String
