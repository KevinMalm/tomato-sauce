from enum import Enum
from lancedb import DBConnection
from lancedb.pydantic import LanceModel


class VectorTable(Enum):
    DUMPING_GROUND = "dumping"
    CHARACTER = "character"
    LOCATION = "location"
    # CHAPTER = "chapter"
    # CHAPTER_XREF = "chapter_xref"
