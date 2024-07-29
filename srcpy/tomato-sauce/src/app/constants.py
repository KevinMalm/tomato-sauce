from enum import Enum


class BackendConstants:
    HOST = "0.0.0.0"
    PORT = 5001

    GET = "GET"
    POST = "POST"

    STREAM_MIME_TYPE = "text/event-stream"
    UTF_8_ENCODING = "utf-8"

    @staticmethod
    def is_post(request):
        return request.method == BackendConstants.POST


class RouteConstants:
    # Chat
    CHAT = "/llm/chat"
    RAG_REFERENCES = "/llm/references"

    # Characters
    DELETE_CHARACTER = "/character/delete"
    ADD_UPDATE_CHARACTER = "/character/update"
    LIST_CHARACTER = "/character/list"

    # Locations
    DELETE_LOCATION = "/location/delete"
    ADD_UPDATE_LOCATION = "/location/update"
    LIST_LOCATION = "/location/list"

    # Chapters
    LIST_CHAPTER_METADATA = "/chapters/metadata"
    CHAPTER_CONTENT = "/chapters/content"
    CHAPTER_CONTENT_ID_PARAMETER = "id"
    DELETE_CHAPTER = "/chapters/delete"


class AvailableInterface(Enum):
    Ollama = "Ollama"
    AwsBedrock = "AWS Bedrock"
    OpenAI = "Open-AI"
