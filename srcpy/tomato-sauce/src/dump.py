from interface import TomatoInterface
from interface.db.constants import VectorTable

with open(
    "../../config/demo/sample/frankenstein_demo/frankenstein_demo.tomato",
    "rb",
) as f:
    interface = TomatoInterface.open(f)

with open("dump_out.txt", "w") as f:
    tbl = interface.database.table(VectorTable.DUMPING_GROUND)
    for r in tbl.search().limit(0).to_list():
        f.write(", ".join([r["tag"], r["key"], r["content"]]) + "\n")
