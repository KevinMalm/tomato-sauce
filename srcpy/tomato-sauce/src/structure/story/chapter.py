from dataclasses import dataclass
from typing import List
from shared.types import String, Number, uuid
from .entity import Entity
from ._abstract import TomatoModel, DumpKeys


@dataclass
class Chapter(TomatoModel):

    @dataclass
    class Metadata:
        id: String
        title: String
        index: Number  # Chapter Index for sorting & re-ordering
        summary: String  # Summary gets chunked in the Vector Database

        involved_characters: List[Entity]
        involved_locations: List[Entity]

    content: String
    metadata: Metadata

    @staticmethod
    def new(title: String):
        return Chapter(
            metadata=Chapter.Metadata(
                id=uuid(),
                title=title,
                index=None,
                summary=String(""),
                involved_characters=[],
                involved_locations=[],
            ),
            content={},
        )

    def sanitize(self):
        self.metadata.id.sanitize()
        self.metadata.title.sanitize()
        self.metadata.summary.sanitize()

    def add_character(self, character: Entity):
        self.metadata.involved_characters.append(character)

    def add_location(self, location: String):
        self.metadata.involved_locations.append(location)

    def into_dumping_attribute(self, chunk):
        return TomatoModel.into_dumping(
            String(chunk),
            [DumpKeys.CHAPTER_GROUP, DumpKeys.CONTENT_SUBGROUP],
            self.metadata.id,
            self.metadata.index.number,
        )
