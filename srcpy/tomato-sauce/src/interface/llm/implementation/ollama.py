from ollama import Client
from lancedb.embeddings import EmbeddingFunction, get_registry
from structure.rest import ChatConversation
from shared.logging import debug
from shared.util import to_json
from ..llm_interface import LargeLangueModelInterface


class OllamaInterface(LargeLangueModelInterface):
    client: Client
    id = "ollama-interface-v1"
    _embedding_function = None

    def connect(self):
        super().connect()
        _host = self.settings.ollama.host.string
        self.client = Client(host=_host)
        debug(f"Now connecting to {_host}")

    def get_config(self):
        return {
            "temperature": self.settings.global_mutable.temperature.number,
            "top_k": self.settings.global_mutable.top_k.number,
            "top_p": self.settings.global_mutable.top_p.number,
        }

    def chat(self, messages: ChatConversation):
        super().chat(messages)
        content = to_json(messages)
        return self.client.chat(
            model=self.settings.global_immutable.model.string,
            messages=content["chats"],
            stream=True,
            options=self.get_config(),
        )

    def embedding_function(self) -> EmbeddingFunction:
        if self._embedding_function is None:
            fn = get_registry().get("ollama")
            self._embedding_function = fn.create(
                name=self.settings.global_immutable.embedding_model.string,
                # name="nomic-embed-text",  # self.settings.global_immutable.model.string,
                host=self.settings.ollama.host.string,
            )
            self._embedding_function.model_fields["host"].default = (
                self.settings.ollama.host.string
            )
        return self._embedding_function
