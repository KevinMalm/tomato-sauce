from ..llm.llm_interface import LargeLangueModelInterface
from structure.error import InternalConsistencyCheckException

EMBEDDING_FUNCTION = None


def get_embedding_function():
    global EMBEDDING_FUNCTION
    if EMBEDDING_FUNCTION is None:
        raise InternalConsistencyCheckException(
            "register_llm_routine",
            "Attempted to access the Embedding Function before a reference was registered",
        )
    return EMBEDDING_FUNCTION


def register_llm(interface: LargeLangueModelInterface):
    global EMBEDDING_FUNCTION
    EMBEDDING_FUNCTION = interface.embedding_function()
