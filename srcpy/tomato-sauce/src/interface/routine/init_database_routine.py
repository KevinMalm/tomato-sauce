from ..db.db_interface import VectorDatabaseInterface
from ..db.constants import VectorTable


def init_database(interface: VectorDatabaseInterface):
    from ..db.table import DumpTable

    for table, model in [
        (VectorTable.DUMPING_GROUND, DumpTable),
    ]:
        interface.loaded_table[table] = interface.connection.create_table(
            name=table.value, schema=model, exist_ok=True
        )
