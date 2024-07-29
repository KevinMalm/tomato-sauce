import dacite.exceptions
import yaml
import dacite
from io import TextIOWrapper
from dataclasses import dataclass

import yaml.scanner
from shared.types import String, Number
from structure.error import FileLoadError


@dataclass
class TomatoSettings:

    @dataclass
    class GlobalImmutableSettings:
        """
        Settings that can only be defined once per project
        """

        interface_option: String
        model: String

    @dataclass
    class GlobalSettings:
        """
        Shared settings across interfaces that can be edited
        """

        linearization: String
        temperature: Number
        top_k: Number
        top_p: Number

    @dataclass
    class OllamaSettings:
        """
        Configuration for Ollama
        """

        host: String

    @dataclass
    class BedrockSettings:
        """
        Configuration for AWS Bedrock
        """

        host: String
        api_key: String

    @dataclass
    class OpenAiSettings:
        """
        Configuration for Open-AI
        """

        host: String
        api_key: String

    global_mutable: GlobalSettings
    global_immutable: GlobalImmutableSettings
    ollama: OllamaSettings
    bedrock: BedrockSettings
    open_ai: OpenAiSettings

    @staticmethod
    def from_file(f: TextIOWrapper):
        try:
            data = yaml.safe_load(f)
            return dacite.from_dict(TomatoSettings, data)
        except Exception as e:
            raise FileLoadError(f.name, "TomatoSettings", str(e))
