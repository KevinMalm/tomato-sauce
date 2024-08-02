from .linearization import ContentLinearization, List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from shared.types import String


class StandardLinearization(ContentLinearization):
    TAG = "Standard Linearization"
    _splitter = None

    def setup(self):
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False,
        )

    def call(self, content: String) -> List[str]:
        if self._splitter is None:
            self.setup()
        return self._splitter.split_text(content.string)
