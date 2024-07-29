from dataclasses import dataclass
from typing import List
from shared.types import String, Number, uuid
from ._abstract import TomatoModel, DumpKeys


@dataclass
class Entity(TomatoModel):
    id: String
    index: Number
    name: String
    summary: String
    aliases: List[String]
    descriptions: List[String]
    relations: List[String]

    @staticmethod
    def new(name: str, summary=""):
        return Entity(
            id=uuid(),
            name=String(name),
            summary=String(summary),
            index=None,
            aliases=[],
            descriptions=[],
            relations=[],
        )

    def sanitize(self):
        self.id.sanitize()
        self.name.sanitize()
        self.summary.sanitize()
        for arr in [self.aliases, self.descriptions, self.relations]:
            for a in arr:
                a.sanitize()

    def add_description(self, description: String):
        self.descriptions.append(description)

    def add_relation(self, relation: String):
        self.relations.append(relation)

    def as_dumping_attributes(self, header: str):
        for alias in self.aliases:
            yield TomatoModel.into_dumping(
                alias, [header, DumpKeys.ALIAS_SUBGROUP], self.id
            )
        for description in self.descriptions:
            yield TomatoModel.into_dumping(
                description,
                [header, DumpKeys.DESCRIPTION_SUBGROUP],
                self.id,
            )
        for relation in self.relations:
            yield TomatoModel.into_dumping(
                relation,
                [header, DumpKeys.RELATION_SUBGROUP],
                self.id,
            )
