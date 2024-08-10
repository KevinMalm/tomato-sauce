import os
from typing import List
from dataclasses import dataclass
import lancedb
from structure import TomatoProject
from structure.story import DumpKeys
from lancedb.pydantic import LanceModel
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

    # loaded_table: dict[VectorTable, Table]
    table_builders: dict[VectorTable, LanceModel]
    content_linearization: ContentLinearization

    def __init__(self, path: str, linearization: ContentLinearization):
        self.path = path
        self.content_linearization = linearization
        self.connection = lancedb.connect(self.path)
        # self.loaded_table = {}
        self.table_builders = {}

    def table(self, name: VectorTable) -> Table:
        return self.connection.create_table(
            name=name.value, schema=self.table_builders[name], exist_ok=True
        )

    def lookup(
        self, content: str, filters=None, limit=10, max_distance=None
    ) -> List[LookupResult]:
        DISTANCE = "_distance"
        q = (
            self.table(VectorTable.DUMPING_GROUND)
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
