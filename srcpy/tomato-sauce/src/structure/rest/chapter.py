from dataclasses import dataclass
from typing import List
from structure.story import Chapter
from shared.types import String, Number


@dataclass
class AddChapterRequest:
    id: String
    title: String
    index: Number
    summary: String

    def into_chapter(self):
        return Chapter(
            content=String(""),
            metadata=Chapter.Metadata(
                id=self.id,
                title=self.title,
                index=self.index,
                summary=self.summary,
                involved_characters=[],
                involved_locations=[],
            ),
        )


@dataclass
class ListChapterMetadataResponse:
    entities: List[Chapter.Metadata]


@dataclass
class DeleteChapterRequestResponse:
    ids: List[str]


@dataclass
class ChapterContent:
    id: String
    content: String
