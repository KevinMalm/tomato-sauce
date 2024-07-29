from typing import List
from structure.error import UnimplementedFunctionException
from shared.types import String


class ContentLinearization:
    TAG = "Content-Abstract"

    def setup(self):
        pass

    def call(self, content: String) -> List[str]:
        UnimplementedFunctionException("linearization", "call(str)")
