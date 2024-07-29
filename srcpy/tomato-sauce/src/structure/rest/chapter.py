from dataclasses import dataclass
from typing import List
from structure.story import Chapter
from shared.types import String


@dataclass
class ListChapterMetadataResponse:
    entities: List[Chapter]


@dataclass
class DeleteChapterRequestResponse:
    ids: List[str]


@dataclass
class ChapterContent:
    id: String
    content: String
