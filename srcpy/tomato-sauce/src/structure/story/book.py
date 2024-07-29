from dataclasses import dataclass
from typing import List
from shared.types import String, Number
from shared.logging import warn, info, debug
from .chapter import Chapter
from .entity import Entity
from structure.error import InternalConsistencyCheckException
from result import Ok, Err, Result


@dataclass
class Book:
    title: String
    author: String
    summary: String

    chapters: List[Chapter]
    chapters_by_key: dict[String, Chapter]

    characters: dict[String, Entity]
    character_names: List[String]
    locations: dict[String, Entity]
    location_names: List[String]

    @staticmethod
    def empty(title: String, author: String):
        return Book(
            title=title,
            author=author,
            summary=String.empty(),
            chapters=[],
            chapters_by_key={},
            characters={},
            character_names=[],
            locations={},
            location_names=[],
        )

    # -- Internal Alignment Functions
    def align(self):
        self._align_chapter_indexes()
        self._align_character_indexes()
        self._align_location_indexes()

    def _align_chapter_indexes(self):
        self.chapters_by_key = {}
        for i, c in enumerate(self.chapters):
            c.metadata.index.number = i
            self.chapters_by_key[c.metadata.id] = c

    def _align_character_indexes(self):
        indexes = [(c.id, c.index.number) for c in self.characters.values()]
        indexes.sort(key=lambda x: x[1])
        for i, (id, _index) in enumerate(indexes):
            self.characters[id].index.number = i
        self.character_names = [c.name for c in self.characters.values()]

    def _align_location_indexes(self):
        indexes = [(c.id, c.index.number) for c in self.locations.values()]
        indexes.sort(key=lambda x: x[1])
        for i, (id, _index) in enumerate(indexes):
            self.locations[id].index.number = i
        self.location_names = [c.name for c in self.locations.values()]

    # -- Begin Chapter CRUD Operations
    def insert_chapter(self, chapter: Chapter) -> Result[bool, str]:
        chapter.sanitize()
        chapter.metadata.index = (
            Number(len(self.chapters))
            if chapter.metadata.index is None
            else chapter.metadata.index
        )
        self.chapters.insert(chapter.metadata.index.number, chapter)
        info("Now adding new Chapter `%s`", chapter.metadata.title)
        self._align_chapter_indexes()
        return Ok(True)

    def update_chapter(self, chapter: Chapter) -> Result[bool, str]:
        chapter.sanitize()
        if chapter.metadata.index.number < 0 or chapter.metadata.index.number >= len(
            self.chapters
        ):
            msg = f"Invalid Chapter index {chapter.metadata.index.number} for {chapter.metadata.title}"
            warn(msg)
            return Err(msg)
        self.chapters.insert(chapter.metadata.index.number, chapter)
        debug("Now updating chapter `%s`", chapter.title)
        self._align_chapter_indexes()
        return Ok(True)

    def delete_chapter(self, id: str) -> Result[Chapter, str]:
        id: String = String(id)
        if id not in self.chapters_by_key:
            msg = f"Failed to get Chapter with the ID {id}"
            warn("book::get_chapter", msg)
            return Err(msg)
        chapter = self.chapters_by_key[id]
        debug("Now deleting chapter `%s`", chapter.metadata.title)
        self.chapters.pop(chapter.metadata.index.number)
        self._align_chapter_indexes()
        return Ok(chapter)

    def get_chapter(self, id: str) -> Result[Chapter, str]:
        id: String = String(id)
        if id not in self.chapters_by_key:
            msg = f"Failed to get Chapter with the ID {id}"
            warn("book::get_chapter", msg)
            Err(msg)
        return Ok(self.chapters_by_key[id])

    # -- Begin Character CRUD Operations
    def add_character(self, character: Entity) -> Result[bool, str]:
        character.sanitize()
        character.index = (
            Number(len(self.characters)) if character.index is None else character.index
        )
        if character.name in self.character_names:
            msg = f"Refused to insert a new Chapter with the duplicated name {character.name}"
            warn(msg)
            return Err(msg)
        self.characters[character.id] = character
        info("Now adding new Character `%s`", character.name)
        self._align_character_indexes()
        return Ok(True)

    def update_character(self, character: Entity) -> Result[bool, str]:
        character.sanitize()
        if character.id not in self.characters:
            msg = f"Failed to fnd the character with the name {character.name}"
            warn(f"{msg} ({character.id})")
            return Err(msg)
        self.characters[character.id] = character
        debug("Now updating character `%s`", character.name)
        self._align_character_indexes()
        return Ok(True)

    def delete_character(self, id: String) -> Result[bool, str]:
        if id not in self.characters:
            msg = f"Failed to find the character with the id {id}"
            warn(msg)
            return Err(msg)
        debug("Now deleting character `%s`", id)
        self.characters.pop(id)
        self._align_chapter_indexes()
        return Ok(True)

    # -- Begin Location CRUD Operations
    def add_location(self, location: Entity) -> Result[bool, str]:
        location.sanitize()
        location.index = (
            Number(len(self.locations)) if location.index is None else location.index
        )
        if location.name in self.location_names:
            msg = f"Refused to insert a new location with the duplicated name {location.name}"
            warn(f"{msg} ({location.id})")
            return Err(msg)
        self.locations[location.id] = location
        info("Now adding new location `%s`", location.name)
        self._align_location_indexes()
        return Ok(True)

    def update_location(self, location: Entity) -> Result[bool, str]:
        location.sanitize()
        if location.id not in self.locations:
            msg = f"Failed to find the location with the name {location.name}"
            warn(f"{msg} ({location.id})")
            return Err(msg)
        self.locations[location.id] = location
        debug("Now updating location `%s`", location.name)
        self._align_location_indexes()
        return Ok(True)

    def delete_location(self, id: String) -> Result[bool, str]:
        if id not in self.locations:
            msg = f"Failed to find the location with the id {id}"
            warn(msg)
            return Err(msg)
        debug("Now deleting location `%s`", id)
        self.locations.pop(id)
        self._align_location_indexes()
        return True
