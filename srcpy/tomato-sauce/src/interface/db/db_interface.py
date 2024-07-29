import os
from typing import List
from dataclasses import dataclass
import lancedb
from structure import TomatoProject, TomatoSettings
from structure.story import DumpKeys
from shared.util import strip_string
from lancedb.table import Table
from lancedb import DBConnection
from .constants import VectorTable
from .chunker import ContentLinearization, build_chunking_linearization_object


class VectorDatabaseInterface:
    @dataclass
    class LookupResult:
        content: str
        distance: float

    path: str
    connection: DBConnection

    loaded_table: dict[VectorTable, Table]
    content_linearization: ContentLinearization

    def __init__(self, path: str, linearization: ContentLinearization):
        self.path = path
        self.content_linearization = linearization
        self.connection = lancedb.connect(self.path)
        self.loaded_table = {}

    def table(self, name: VectorTable) -> Table:
        return self.loaded_table[name]

    def lookup(
        self, content: str, filters=None, limit=10, max_distance=None
    ) -> List[LookupResult]:
        DISTANCE = "_distance"
        q = (
            self.loaded_table[VectorTable.DUMPING_GROUND]
            .search(query=content, vector_column_name=DumpKeys.VECTOR)
            .limit(limit)
        )
        if filters is not None:
            q.where(filters, prefilter=True)
        return [
            VectorDatabaseInterface.LookupResult(r[DumpKeys.CONTENT], r[DISTANCE])
            for r in q.to_list()
            if max_distance is None or r[DISTANCE] < max_distance
        ]

    @staticmethod
    def init(metadata: TomatoProject.ProjectMetaData):
        path = os.path.join(
            metadata.path.string,
            strip_string(metadata.file_name.string),
        )
        linearization = build_chunking_linearization_object(
            metadata.settings.global_mutable.linearization
        )
        return VectorDatabaseInterface(path, linearization)
