from interface.db.db_interface import VectorDatabaseInterface
from structure.rest import ChatConversation, ChatEntry
from ..prompt_interface import PromptInterface


class NoRagChatPromptInterface(PromptInterface):

    def __init__(self, template: str, interface: VectorDatabaseInterface) -> None:
        super().__init__(template, interface)

    def inject(self, content: ChatConversation) -> ChatConversation:
        content.chats.insert(0, ChatEntry.system(self.template))
        return content
