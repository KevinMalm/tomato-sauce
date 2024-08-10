from structure import TomatoProject, TomatoSettings
from shared.logging import info
from structure.error import InternalConsistencyCheckException
from app import AvailableInterface
from .implementation.ollama import OllamaInterface
from .implementation.bedrock import AwsBedrockInterface


def init_llm(metadata: TomatoProject.ProjectMetaData):
    info(
        "Initializing an LLM Interface for %s",
        metadata.settings.global_immutable.interface_option,
    )
    match metadata.settings.global_immutable.interface_option.string:
        case AvailableInterface.Ollama.value:
            return OllamaInterface(metadata.settings)
        case AvailableInterface.AwsBedrock.value:
            return AwsBedrockInterface(metadata.settings)

    raise InternalConsistencyCheckException(
        "llm_builder",
        f"Unsupported Interface {metadata.settings.global_immutable.interface_option}",
    )
