from interface.db.db_interface import VectorDatabaseInterface
from structure.rest import ChatConversation, ChatEntry
from ..prompt_interface import PromptInterface


class RagChatPromptInterface(PromptInterface):

    def __init__(self, template: str, interface: VectorDatabaseInterface) -> None:
        super().__init__(template, interface)

    def inject(self, content: ChatConversation) -> ChatConversation:
        _context = content.chats[-1].content
        self.context = RagChatPromptInterface.PriorContext(
            _context, self.interface.lookup(_context, limit=1000)
        )
        prompt = self.template.format(
            content="\n- ".join([l.content for l in self.context.lookups])
        )
        content.chats.insert(0, ChatEntry.system(prompt))
        return content
