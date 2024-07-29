from interface.db.chunker import StandardLinearization, ContentLinearization
from structure.error import InternalConsistencyCheckException
from shared.types import String


def build_chunking_linearization_object(method: String) -> ContentLinearization:

    for cls in [StandardLinearization]:
        cls: ContentLinearization = cls
        if method.string == cls.TAG:
            return cls()

    raise InternalConsistencyCheckException(
        "build_linearization_routine",
        f"Unsupported Chunking Strategy `{method.string}`",
    )
