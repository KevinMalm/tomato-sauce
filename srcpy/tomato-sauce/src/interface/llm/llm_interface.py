from shared.logging import info, debug
from lancedb.embeddings import EmbeddingFunction
from structure.rest import ChatConversation
from structure.error import UnimplementedFunctionException
from structure import TomatoSettings


class LargeLangueModelInterface:
    id: str = "abstract0interface"
    settings: TomatoSettings

    def __init__(self, settings: TomatoSettings):
        self.settings = settings
        self.connect()

    def connect(self):
        info("Now Connecting... (%s)", self.id)

    def chat(self, messages: ChatConversation):
        for msg in messages.chats:
            debug(msg)

    def embedding_function(self) -> EmbeddingFunction:
        raise UnimplementedFunctionException("llm_interface", "embedding_function")
