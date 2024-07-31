from dataclasses import dataclass
from .prompt_interface import PromptTag
import interface.prompt.interfaces as Interfaces


@dataclass
class PromptRepositoryBuilder:
    template: str
    builder: object


class PromptRepository:
    prompts = {
        PromptTag.NoRAGChatPrompt: PromptRepositoryBuilder(
            """
You are a helpful Co-Author helping write a book. 
""",
            Interfaces.NoRagChatPromptInterface,
        ),
        PromptTag.StandardChatPrompt: PromptRepositoryBuilder(
            """
You are a helpful Co-Author helping write a book.
Answer all questions ONLY off the provided context. If you are unsure of the answer, respond with "I am unsure" instead of making up a response.
Think carefully before answering and put any thoughts in a <scratchpad> block.
<context>:
- {content}
<context>
""",
            Interfaces.RagChatPromptInterface,
        ),
    }
