from threading import Thread
import time
from typing import Callable
from structure.story.book import Book
from shared.types import String
from structure.story import DumpKeys, Chapter
from ..llm import LargeLangueModelInterface
from ..db import VectorDatabaseInterface
from ..db.constants import VectorTable
from shared.logging import debug
from result import Ok, Err, Result
from app import set_thinking_stage


class BookRoutine:

    book: Book
    database: VectorDatabaseInterface
    save: Callable

    def __init__(
        self,
        book: Book,
        database: VectorDatabaseInterface,
        save: Callable,
    ):
        self.book = book
        self.database = database
        self.save = save

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
