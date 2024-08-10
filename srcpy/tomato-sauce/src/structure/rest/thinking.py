from dataclasses import dataclass


@dataclass
class ThinkingState:
    thinking: bool
    message: str
