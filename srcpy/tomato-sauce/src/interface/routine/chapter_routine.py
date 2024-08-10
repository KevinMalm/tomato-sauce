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


class ChapterRoutine:

    book: Book
    database: VectorDatabaseInterface
    llm: LargeLangueModelInterface
    save: Callable

    def __init__(
        self,
        book: Book,
        database: VectorDatabaseInterface,
        llm: LargeLangueModelInterface,
        save: Callable,
    ):
        self.book = book
        self.database = database
        self.llm = llm
        self.save = save

    def _clear_content(self, id: str = None, chapter: Chapter = None):
        chapter = self.book.get_chapter(id) if chapter is None else chapter
        d_tbl = self.database.table(VectorTable.DUMPING_GROUND)
        _statement = f"{DumpKeys.KEY} = '{chapter.metadata.id}' AND {DumpKeys.TAG} LIKE '{DumpKeys.CHAPTER_GROUP}/%'"
        debug(f"({VectorTable.DUMPING_GROUND}) Executing DELETE {_statement}")
        d_tbl.delete(_statement)

    def clear(self, id: str = None, chapter: Chapter = None):
        self._clear_content(id, chapter)
        return

    def _add_content(self, chapter: Chapter):
        d_tbl = self.database.table(VectorTable.DUMPING_GROUND)
        chunks = [
            chapter.into_dumping_attribute(c)
            for c in self.database.content_linearization.call(chapter.content)
        ]
        debug(f"{chapter.metadata.title} broken down into {len(chunks)} chunks...")
        if len(chunks) > 0:
            d_tbl.add(chunks)
        return len(chunks)

    def _add(self, chapter: Chapter):
        if chapter.content is not None or len(chapter.content) == 0:
            self._add_content(chapter)

    def add(self, chapter: Chapter) -> Result[bool, str]:
        match self.book.insert_chapter(chapter):
            case Err(e):
                return Err(e)
        self._add(chapter)
        return Ok(True)

    def update_content(self, chapter: Chapter):
        def threaded_update(chapter: Chapter):
            set_thinking_stage(True, message=f"Rehashing {chapter.metadata.title}")
            self._clear_content(chapter=chapter)
            cnt = self._add_content(chapter=chapter)
            set_thinking_stage(
                False, message=f"update_content {cnt} / {chapter.metadata.title}"
            )
            return

        _thread = Thread(target=threaded_update, args=(chapter,))
        _thread.start()

    def update_metadata(self, chapter: Chapter):
        """if self.book.update_chapter(chapter) is False:
            return False
        self._clear_metadata(chapter.id.string, chapter)
        self._add_metadata(chapter)
        return True"""
        pass

    def delete(self, id: str) -> Result[bool, str]:
        match self.book.delete_chapter(id):
            case Err(e):
                return Err(e)
            case Ok(x):
                self.clear(chapter=x)

    def list_all_metadata(self):
        return [c.metadata for c in self.book.chapters]

    def get_content(self, id: str) -> Result[str, str]:
        id: String = String(id)
        if id not in self.book.chapters_by_key:
            return Err(f"Failed to find Chapter with ID {id}")
        return Ok(self.book.chapters_by_key[id].content)

    def set_content(self, id: str, content: dict) -> Result[bool, str]:
        id: String = String(id)
        if id not in self.book.chapters_by_key:
            return Err(f"Failed to find Chapter with ID {id}")
        chapter = self.book.chapters_by_key[id]
        chapter.content = content
        self.update_content(chapter)
        self.save()
        return Ok(True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


"""
    def _add_metadata(self, chapter: Chapter):
        c_tbl = self.database.table(VectorTable.CHAPTER)
        c_tbl.add([chapter.as_specific_attributes()])
        x_tbl = self.database.table(VectorTable.CHAPTER_XREF)
        x_tbl.add(chapter.as_xref_attributes())

        
    def _clear_metadata(self, id: str):
        _statement = f"{ChapterKey.ID} = '{id}'"

        c_tbl = self.database.table(VectorTable.CHAPTER)
        debug(f"({VectorTable.CHAPTER}) Executing DELETE {_statement}")
        c_tbl.delete(_statement)

        x_tbl = self.database.table(VectorTable.CHAPTER_XREF)
        debug(f"({VectorTable.CHAPTER_XREF}) Executing DELETE {_statement}")
        x_tbl.delete(_statement)
"""
