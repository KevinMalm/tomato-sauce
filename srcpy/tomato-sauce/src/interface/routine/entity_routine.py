from dataclasses import dataclass
from typing import Callable
from result import Ok, Err, Result
from structure.story.book import Book
from structure.story import DumpKeys, Entity
from structure.error import InternalConsistencyCheckException
from ..llm import LargeLangueModelInterface
from ..db import VectorDatabaseInterface
from ..db.constants import VectorTable
from shared.logging import debug
from shared.types import String


class EntityRoutine:

    @dataclass
    class CRUD:
        get: Callable[[String], Result[dataclass, str]]
        add: Callable[[String], Result[bool, str]]
        update: Callable[[String], Result[bool, str]]
        delete: Callable[[String], Result[bool, str]]

    book: Book
    table: VectorTable
    crud: CRUD
    database: VectorDatabaseInterface
    llm: LargeLangueModelInterface

    def __init__(
        self,
        book: Book,
        table: VectorTable,
        crud: CRUD,
        database: VectorDatabaseInterface,
        llm: LargeLangueModelInterface,
    ):
        self.book = book
        self.table = table
        self.crud = crud
        self.database = database
        self.llm = llm

    def get_tag_group(self):
        match self.table:
            case VectorTable.CHARACTER:
                return DumpKeys.CHARACTER_GROUP
            case VectorTable.LOCATION:
                return DumpKeys.LOCATION_GROUP
        raise InternalConsistencyCheckException(
            f"entity_routine::get_tag_group",
            f"Unexpected Group Table {self.config.table}",
        )

    def clear(self, id: str):
        d_tbl = self.database.table(VectorTable.DUMPING_GROUND)
        _statement = f"{DumpKeys.KEY} = '{id}' AND {DumpKeys.TAG} LIKE '{self.get_tag_group()}/%'"
        debug(f"({VectorTable.DUMPING_GROUND}) Executing DELETE {_statement}")
        d_tbl.delete(_statement)

    def _add(self, entity: Entity):
        # Dumping Ground
        d_tbl = self.database.table(VectorTable.DUMPING_GROUND)
        d_tbl.add([c for c in entity.as_dumping_attributes(self.get_tag_group())])

    def add(self, entity: Entity) -> Result[bool, str]:
        match self.crud.add(entity):
            case Err(e):
                return Err(e)
        self._add(entity)
        return Ok(True)

    def update(self, entity: Entity) -> Result[bool, str]:
        match self.crud.update(entity):
            case Err(_):
                return self.add(entity)
        self.clear(entity.id.string)
        self._add(entity)
        return Ok(True)

    def delete(self, id: str) -> Result[bool, str]:
        match self.crud.delete(String(id)):
            case Err(e):
                return Err(e)
        self.clear(id)
        return Ok(True)

    def list_all(self):
        return self.crud.get()

    def find(self, id: str):
        for entity in self.crud.get():
            entity: Entity = entity
            if entity.id.string == id:
                return entity
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


"""
    def clear(self, id: str):
        c_tbl = self.database.table(self.config.table)
        _statement = f"{EntityKeys.ID} = '{id}'"
        debug(f"({self.table}) Executing DELETE {_statement}")
        c_tbl.delete(_statement)

    def _add(self, entity: Entity):
        # Storage Table
        c_tbl = self.database.table(self.config.table)
        c_tbl.add([entity.as_specific_attributes()])
"""
