from dataclasses import dataclass
from typing import List


@dataclass
class ChatEntry:
    role: str
    content: str

    @staticmethod
    def system(content: str):
        return ChatEntry("system", content)


@dataclass
class ChatConversation:
    chats: List[ChatEntry]
    inject_rag: bool
