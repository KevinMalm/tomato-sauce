from dataclasses import dataclass
from typing import List
from structure.story import Entity


@dataclass
class ListEntitiesResponse:
    entities: List[Entity]


@dataclass
class DeleteEntitiesRequestResponse:
    ids: List[str]
