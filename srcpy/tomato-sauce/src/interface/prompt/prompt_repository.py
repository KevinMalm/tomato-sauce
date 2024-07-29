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
- {content}
""",
            Interfaces.RagChatPromptInterface,
        ),
    }
