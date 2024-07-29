from typing import List

from shared.types import String


class DumpKeys:
    VECTOR = "vector"
    CONTENT = "content"
    TAG = "tag"
    KEY = "key"
    INDEX = "index"

    CHARACTER_GROUP = "character"
    LOCATION_GROUP = "location"
    CHAPTER_GROUP = "chapter"
    # Entity Specific
    ALIAS_SUBGROUP = "aliases"
    DESCRIPTION_SUBGROUP = "descriptions"
    RELATION_SUBGROUP = "relation"
    # Chapter Specific
    CONTENT_SUBGROUP = "content"


class TomatoModel:
    id: str

    def as_dumping_attributes(self):
        pass

    @staticmethod
    def into_dumping(content: String, tag: List[str], key: String, index: int = 0):
        return {
            DumpKeys.CONTENT: content.string,
            DumpKeys.TAG: "/".join(tag),
            DumpKeys.KEY: key.string,
            DumpKeys.INDEX: index,
        }
