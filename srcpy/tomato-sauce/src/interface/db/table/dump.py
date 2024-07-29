from lancedb.pydantic import LanceModel, Vector
from ...routine import get_embedding_function

FUNCTION = get_embedding_function()


class DumpTable(LanceModel):
    vector: Vector(FUNCTION.ndims()) = FUNCTION.VectorField()  # type: ignore
    content: str = FUNCTION.SourceField()
    tag: str
    key: str
    index: int
