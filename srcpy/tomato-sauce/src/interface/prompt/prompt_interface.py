from enum import Enum
from dataclasses import dataclass
from typing import List
from interface.db import VectorDatabaseInterface
from structure.error import UnimplementedFunctionException
from structure.rest import ChatConversation


class PromptTag(Enum):
    NoRAGChatPrompt = "no-rag-chat-prompt"
    StandardChatPrompt = "standard-chat-prompt"


class PromptInterface:

    @dataclass
    class PriorContext:
        context: str
        lookups: List[VectorDatabaseInterface.LookupResult]

    template: str
    vdb: VectorDatabaseInterface
    context: PriorContext

    def __init__(self, template: str, interface: VectorDatabaseInterface) -> None:
        self.template = template
        self.interface = interface
        self.context = None

    def inject(self, content: ChatConversation) -> ChatConversation:
        raise UnimplementedFunctionException("prompt_interface.py", "inject")
