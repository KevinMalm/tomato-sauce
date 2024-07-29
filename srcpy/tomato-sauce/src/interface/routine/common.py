from lancedb.table import Table
from structure.story import DumpKeys
from structure.error import InternalConsistencyCheckException


def get_specific_attributes(tbl: Table, id_field):
    for element in tbl.search().to_list():
        yield element[id_field], element


def get_dumping_attributes(tbl: Table, tag: str):
    for element in tbl.search().where(f"tag LIKE '{tag}/%'").limit(0).to_list():
        key = element[DumpKeys.KEY]
        tag = element[DumpKeys.TAG]

        if DumpKeys.ALIAS_SUBGROUP in tag:
            yield DumpKeys.ALIAS_SUBGROUP, (key, element)
            continue
        if DumpKeys.DESCRIPTION_SUBGROUP in tag:
            yield DumpKeys.DESCRIPTION_SUBGROUP, (key, element)
            continue
        if DumpKeys.RELATION_SUBGROUP in tag:
            yield DumpKeys.RELATION_SUBGROUP, (key, element)
            continue

        raise InternalConsistencyCheckException(
            "character_routine::list_all::get_dumping_attributes",
            f"Unexpected Character Tag {tag} for ID {key}",
        )
